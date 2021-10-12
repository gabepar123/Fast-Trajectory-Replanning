import random


class Cell:

    #determines if the cell is blocked or not
    is_blocked = False
    #represents a states f/h/g values for A*
    # f(n) = h(n) + g(n)
    f = 0
    h = 0
    g = 0
    
    #THIS IS ONLY FOR PRINTING THE MAZE
    print_char = "-"

    def __init__(self, f, h, g, is_blocked):
        self.f = f
        self.h = h
        self.g = g
        self.is_blocked = is_blocked

#
# Creates a maze using a 2D Array of the Cell class
#   
#
class Maze:

    MAZE_SIZE = 101 # Change this to change maze dimensions
    maze = [[]]

    # Default goal pos = [100][100]
    GOAL_X = MAZE_SIZE - 1
    GOAL_Y = MAZE_SIZE - 1
    #Agent starting pos = [0][0]
    agent_pos_x = 0
    agent_pos_y = 0
    

    def __init__(self):
        
        self.maze = [[Cell(0,0,0,False) for j in range(self.MAZE_SIZE)] for i in range(self.MAZE_SIZE)]

    def print_maze(self):
        for row in self.maze:
            print("[", end ="")
            for col in row:
                print(col.print_char, end = "")
            print("]")

    #
    # Creates grid world using stack DFS
    # Marking the index as "-" corresponds to UNBLOCKED, only for printing
    # Marking the index as "█" corresponds to BLOCKED, only for printing
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
                self.maze[row][col].is_blocked == True
                self.maze[row][col].print_char = "█"
