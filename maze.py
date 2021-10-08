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
    GOAL = [MAZE_SIZE - 1, MAZE_SIZE - 1]
    #Agent starting pos = [0][0]
    agent_pos = [0, 0]
    

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
        visited[0][0] = visited[self.MAZE_SIZE - 1][self.MAZE_SIZE - 1] = True
        self.maze[0][0].print_char = "A"
        self.maze[self.MAZE_SIZE - 1][self.MAZE_SIZE - 1].print_char = "G"

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

            



    #TODO: delete this or finish it
    def create_maze_backtracking(self):
        global maze
        visited = [[False]*MAZE_SIZE for _ in range(MAZE_SIZE)]

        row = start_row = random.randint(0, MAZE_SIZE - 1)
        col = start_col = random.randint(0, MAZE_SIZE - 1)

        st = []
        st.append([start_row, start_col])
        visited[start_row][start_col] = True

        while (len(st) > 0):
            curr = st.pop()
            row = curr[0]
            col = curr[1]
            
            #if (row < 0 or row >= MAZE_SIZE or col < 0 or col >= MAZE_SIZE or visited[row][col]):
            #    continue
            
            #visited[row][col] = True

            neighbors = []

            if row + 1 < MAZE_SIZE and not visited[row + 1][col]:
                neighbors.append([row + 1, col])
            if row - 1 >= 0 and not visited[row - 1][col]:
                neighbors.append([row - 1, col])
            if col + 1 < MAZE_SIZE and not visited[row][col + 1]:
                neighbors.append([row, col + 1])
            if col - 1 >= 0 and not visited[row][col - 1]:
                neighbors.append([row, col - 1])
            
            if len(neighbors) > 0:
                #st.append([row, col])
                chosen_neighbor = neighbors[random.randint(0, len(neighbors) - 1)]
            # for n in neighbors:
            #     if n != chosen_neighbor:
            #         visited[n[0]][n[1]] = True
                maze[row][col] = "-"
                maze[chosen_neighbor[0]][chosen_neighbor[1]] = "-"
                visited[chosen_neighbor[0]][chosen_neighbor[1]] = True
                st.append(chosen_neighbor)
