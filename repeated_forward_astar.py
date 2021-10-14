from min_heap import *
from maze import *
import math
import random
import time

class repeated_forward_astar():

     
    def __init__(self, use_small_g):
        self.use_small_g = use_small_g
        self.m = Maze()
        self.m.create_maze_dfs()
        #self.m.print_maze()
        self.cells_expanded = 0
        self.closed = set()


    def new_maze(self):
        self.m = self.m.create_maze_dfs()

    def compute_path(self, start_cell, goal_cell, open, counter):
        while goal_cell.g > open.peek():
            curr_cell = open.delete()
            self.closed.add(curr_cell)

            neighbors = self.find_valid_neighbors(curr_cell)
            for succ in neighbors:
                if succ.search < counter:
                    succ.g = math.inf #Infinity
                    succ.search = counter
                if succ.g > curr_cell.g + curr_cell.cost:
                    succ.g = curr_cell.g + curr_cell.cost

                    succ.pointer = curr_cell #Update tree pointer

                    open.deleteItem(succ)

                    succ.h = self.compute_h_value(succ)
                    succ.f = succ.g + succ.h
                    open.insert(succ)
            if open.size() == 0: return
        
        

    def run(self):
        time_start = time.time()

        counter = 0

        start_x = self.m.agent_pos_x
        start_y = self.m.agent_pos_y
        start_cell = self.m.maze[start_x][start_y] # holds Cell object of current maze index
        goal_cell = self.m.maze[self.m.GOAL_X][self.m.GOAL_Y]  #holds Cell object of GOAL maze index

        while start_cell is not goal_cell:
            counter += 1

            start_cell.g = 0  # initial g value
            start_cell.search = counter
            goal_cell.g = math.inf # GOAl G value
            goal_cell.search = counter

            open = Heap(self.use_small_g)
            self.cells_expanded += len(self.closed) 
            self.closed = set() #set() = hashSet O(1) search

            start_cell.h = self.compute_h_value(start_cell)
            start_cell.f = start_cell.g + start_cell.h #f value
            open.insert(start_cell)
            
            self.compute_path(start_cell, goal_cell, open, counter)
            
            if open.size() == 0:
                #print("Cannot reach Target!")
                return (time.time() - time_start), self.cells_expanded

            tree_pointer = goal_cell
            backtrack = [] #Saves the Cells the tree pointers follow, used to update Agent's location
            while tree_pointer is not start_cell: #Follow pointers from goal -> start
                backtrack.append(tree_pointer)
                tree_pointer = tree_pointer.pointer
            
            backtrack.reverse() #Reverse list to follow it from start -> goal
            for cell in backtrack: #Update agent state until we hit a blocked cell
                if cell.is_blocked:
                    #action_cost += 1
                    cell.cost = math.inf
                    break
                start_cell = cell
        #print("Target reached!")
        return (time.time() - time_start), self.cells_expanded



    def compute_h_value(self, cell):
        return abs(cell.x_pos - self.m.GOAL_X) + abs(cell.y_pos - self.m.GOAL_Y)


    # adds all neighbors that havent been expanded yet (closed list)
    def find_valid_neighbors(self, curr_cell):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                row = curr_cell.x_pos
                col = curr_cell.y_pos
                if (i == 0 or j == 0) and i != j:
                    row += i
                    col += j
                    #if (0 <= row < m.MAZE_SIZE and 0 <= col < m.MAZE_SIZE and not m.maze[row][col] in closed):
                    if (row >= 0 and row < self.m.MAZE_SIZE and col >= 0 and col < self.m.MAZE_SIZE and not self.m.maze[row][col] in self.closed):
                        neighbors.append(self.m.maze[row][col])
        return neighbors
        
