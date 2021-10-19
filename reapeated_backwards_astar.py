from min_heap import *
from maze import *
import math
import random
import time

class repeated_backwards_astar():

     
    def __init__(self, use_small_g, visualize, print_status, file_index):
        self.use_small_g = use_small_g
        self.visualize = visualize
        self.print_status = print_status
        self.m = Maze()
        self.m.create_maze_from_file(file_index)
        self.cells_expanded = 0
        self.closed = set()
        self.final_path = []


    def print_final_path(self):
        self.m.print_final_maze(self.final_path)

    def compute_path(self, start_cell, open, counter):
        while start_cell.g > open.peek():
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

                    succ.h = self.compute_h_value(succ, start_cell)
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

            goal_cell.g = 0  # initial g value
            goal_cell.search = counter
            start_cell.g = math.inf # GOAl G value
            start_cell.search = counter

            open = Heap(self.use_small_g)
            self.cells_expanded += len(self.closed) 
            self.closed = set() #set() = hashSet O(1) search

            goal_cell.h = self.compute_h_value(goal_cell, start_cell)
            goal_cell.f = goal_cell.g + goal_cell.h #f value
            open.insert(goal_cell)
            
            self.compute_path(start_cell, open, counter)
            
            if open.size() == 0:
                if self.print_status:
                    print("Cannot reach Target!")
                return (time.time() - time_start), self.cells_expanded

            tree_pointer = start_cell
            while tree_pointer is not goal_cell:
                tree_pointer = tree_pointer.pointer
                if tree_pointer.is_blocked:
                    tree_pointer.cost = math.inf
                    break
                start_cell = tree_pointer
                self.update_all_h_values(start_cell)

                #TODO: final path

        if self.print_status:
            print("Target reached!")
        return (time.time() - time_start), self.cells_expanded

    def compute_h_value(self, cell, start_cell):
        return abs(cell.x_pos - start_cell.x_pos) + abs(cell.y_pos - start_cell.y_pos)

    def update_all_h_values(self, start_cell):
        for row in self.m.maze:
            for cell in row:
                cell.h = self.compute_h_value(cell, start_cell)

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
        
