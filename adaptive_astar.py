from min_heap import *
from maze import *
import math
import time
import matplotlib
import matplotlib.pyplot as plt

class adaptive_astar():

    def __init__(self, use_small_g, visualize, print_status, file_index):
        self.use_small_g = use_small_g
        self.visualize = visualize
        self.print_status = print_status
        self.m = Maze()
        self.m.create_maze_from_file(file_index)
        self.cells_expanded = 0
        self.closed = set()
        if self.visualize:
            self.colors = 'lightgray gray blue red black white yellow'.split()
            self.cmap = matplotlib.colors.ListedColormap(self.colors, name='colors', N=None)
            self.UPDATE_SPEED = 1e-10 #for GUI

    def print_final_path(self):
        self.m.print_final_maze(self.final_path)

    def compute_path(self, goal_cell, open, counter):
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
        if self.visualize:
            self.initialize_gui()

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
            
            self.compute_path(goal_cell, open, counter)

            for cell in self.closed:
                cell.h = goal_cell.g - cell.h #adaptive a*
                cell.f = cell.g + cell.h
            
            if open.size() == 0:
                if self.print_status:
                    print("Cannot reach Target!")
                if self.visualize:
                    plt.show()
                return (time.time() - time_start), self.cells_expanded

            tree_pointer = goal_cell
            backtrack = [] #Saves the Cells the tree pointers follow, used to update Agent's location
            while tree_pointer is not start_cell: #Follow pointers from goal -> start
                backtrack.append(tree_pointer)
                tree_pointer = tree_pointer.pointer

            if self.visualize:
                self.m.update_shortest_path(backtrack, start_cell)

            backtrack.reverse() #Reverse list to follow it from start -> goal
            for cell in backtrack: #Update agent state until we hit a blocked cell
                if self.visualize:
                    self.m.update_int_maze(start_cell)
                    self.update_gui()
                
                if cell.is_blocked:
                    cell.cost = math.inf
                    break
                start_cell = cell

        if self.print_status:
            print("Target reached!")

        if self.visualize:
            plt.show()

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
                    if (row >= 0 and row < self.m.MAZE_SIZE and col >= 0 and col < self.m.MAZE_SIZE and not self.m.maze[row][col] in self.closed):
                        neighbors.append(self.m.maze[row][col])
        return neighbors

    def initialize_gui(self):
        plt.figure(figsize=(9,9))
        self.m.update_int_maze(self.m.maze[self.m.agent_pos_x][self.m.agent_pos_y])
        self.update_gui()

    def update_gui(self):
        plt.cla()
        plt.imshow(self.m.int_maze, cmap=self.cmap)
        plt.pause(self.UPDATE_SPEED)