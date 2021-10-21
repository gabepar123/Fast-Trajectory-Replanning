import random

class Cell:

    def __init__(self, f, h, g, is_blocked):
        #represents a states f/h/g values for A*
        # f(n) = h(n) + g(n)
        self.f = f
        self.h = h
        self.g = g
        self.is_blocked = is_blocked  #determines if the cell is blocked or not
        self.cost = 1
        self.x_pos = 0
        self.y_pos = 0
        self.search = 0
        self.pointer = None
        self.print_char = "-" #THIS IS ONLY FOR PRINTING THE MAZE
        


#
# Creates a maze using a 2D Array of the Cell class
#   
#
class Maze:

    
    def __init__(self):

        self.MAZE_SIZE = 101 # Change this to change maze dimensions

        self.maze = [[Cell(0,0,0,False) for j in range(self.MAZE_SIZE)] for i in range(self.MAZE_SIZE)]
        #sets x and y positions of each cell object
        for i, row in enumerate(self.maze):
            for j, col in enumerate(row):
                col.x_pos = i
                col.y_pos = j

        
        # Default goal pos = [100][100]
        self.GOAL_X = self.MAZE_SIZE - 1
        self.GOAL_Y = self.MAZE_SIZE - 1
        #Agent starting pos = [0][0]
        self.agent_pos_x = 0
        self.agent_pos_y = 0

        #used for visualization
        self.int_maze = [[0 for j in range(self.MAZE_SIZE)] for i in range(self.MAZE_SIZE)]
        self.default_maze = self.int_maze.copy()
        self.UNBLOCKED = 0
        self.BLOCKED = 1
        self.AGENT = 2
        self.GOAL = 3
        self.SEEN_BLOCKED = 4
        self.SEEN_UNBLOCKED = 5
        self.PATH = 6
        #self.PATH_BLOCKED = 7
                    
                
    def print_maze(self):
        for row in self.maze:
            print("[", end ="")
            for col in row:
                print(col.print_char, end = "")
            print("]")
    
    def print_final_maze(self, path):
        
        for cell in path:
            if cell.is_blocked: raise IndexError("Blocked Cell in Final Path!")

            if (cell.x_pos != self.agent_pos_x and cell.y_pos != self.agent_pos_y) or (cell.x_pos != self.GOAL_X and cell.y_pos != self.GOAL_Y):
                self.maze[cell.x_pos][cell.y_pos].print_char = "x"
        
        self.maze[self.agent_pos_x][self.agent_pos_y].print_char = "A"
        self.maze[self.GOAL_X][self.GOAL_Y].print_char = "G"

        self.print_maze()
        print("Path length: %d" % len(path))


    def create_maze_from_file(self, file_index):
        file_name = file_name = "grid_worlds/" + str(file_index) + ".txt"
        f = open(file_name, "r")
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                c = f.read(1)
                if c == "\n":
                    c = f.read(1)
                if c == "x":
                    cell.is_blocked = True
                    cell.print_char = "x"
                    self.int_maze[i][j] = self.BLOCKED
                elif c == "-":
                    cell.print_char = "-"
                    self.int_maze[i][j] = self.UNBLOCKED
                elif c == "A":
                    self.agent_pos_x = i
                    self.agent_pos_y = j
                    cell.print_char = "A"
                    self.int_maze[i][j] = self.AGENT
                elif c == "G":
                    self.GOAL_X = i
                    self.GOAL_Y = j
                    cell.print_char = "G"
                    self.int_maze[i][j] = self.GOAL

        self.default_maze = self.int_maze.copy()

    # UNUSED:
    # Creates grid world using stack DFS
    # Marking the index as "-" corresponds to UNBLOCKED, only for printing
    # Marking the index as "x" corresponds to BLOCKED, only for printing
    # "A" is the Agent's position
    # "G" is the goal index

    def create_maze_dfs(self):
        # make sure to never block the goal or initial position
        visited = [[False for j in range(self.MAZE_SIZE)] for i in range(self.MAZE_SIZE)]
        visited[self.agent_pos_x][self.agent_pos_y] = visited[self.GOAL_X][self.GOAL_Y] = True
        self.maze[self.agent_pos_x][self.agent_pos_y].print_char = "A"
        self.maze[self.GOAL_X][self.GOAL_Y].print_char = "G"

        row = start_row = random.randint(1, self.MAZE_SIZE - 2)
        row = start_col = random.randint(1, self.MAZE_SIZE - 2)

        st = []
        st.append([start_row, start_col])

        while (len(st) > 0):
            curr = st.pop()
            row = curr[0]
            col = curr[1]
            
            if (row < 0 or row >= self.MAZE_SIZE or col < 0 or col >= self.MAZE_SIZE or visited[row][col]):
                continue
            
            visited[row][col] = True

            rand = random.random()
            # we mark an index as unblocked 70% of the time
            # or if it is the first index
            if rand < 0.7 or (row == start_row and col == start_col) :
                #we only add unblocked indexs to the stack
                st.append([row + 1, col])
                st.append([row - 1, col])
                st.append([row, col + 1])
                st.append([row, col - 1])
                
            else:
                self.maze[row][col].is_blocked = True
                self.maze[row][col].print_char = "x"

        #clear out area near goal and agent to reduce chance of it being closed off
        for i in range(0,10):
            for j in range(1,10):
                self.maze[i][j].is_blocked = False
                self.maze[i][j].print_char = "-"
        for i in range(85,100):
            for j in range(85,100):
                self.maze[i][j].is_blocked = False
                self.maze[i][j].print_char = "-"


    # updates seen cells in
    def update_int_maze(self, agent):
        for i in range(-1, 2):
            for j in range(-1, 2):
                row = agent.x_pos
                col = agent.y_pos
                if (i == 0 or j == 0) and i != j:
                    row += i
                    col += j
                    if (row >= 0 and row < self.MAZE_SIZE and col >= 0 and col < self.MAZE_SIZE):
                        if self.maze[row][col].is_blocked:
                            self.int_maze[row][col] = self.SEEN_BLOCKED
                        else:
                            self.int_maze[row][col] = self.SEEN_UNBLOCKED

        if agent.x_pos == 0 and agent.y_pos == 0:
            self.int_maze[0][100] = self.PATH

        self.int_maze[agent.x_pos][agent.y_pos] = self.AGENT
        self.int_maze[self.GOAL_X][self.GOAL_Y] = self.GOAL
    
    #Only for GUI
    #resets maze and shows shortest path
    def update_shortest_path(self, path, agent):

        for row in range(0, self.MAZE_SIZE):
            for col in range(0, self.MAZE_SIZE):
                if self.int_maze[row][col] == self.PATH:
                    if self.maze[row][col].is_blocked:
                        self.int_maze[row][col] = self.BLOCKED
                    else:
                        self.int_maze[row][col] = self.UNBLOCKED

        for cell in path:
            self.int_maze[cell.x_pos][cell.y_pos] = self.PATH

        self.int_maze[agent.x_pos][agent.y_pos] = self.AGENT
        self.int_maze[self.GOAL_X][self.GOAL_Y] = self.GOAL



    



