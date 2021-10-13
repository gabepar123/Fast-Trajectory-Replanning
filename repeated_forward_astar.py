from binary_heap import *
from maze import *
import math
import random

m = Maze()
m.create_maze_dfs()
m.print_maze()

def compute_path(start_cell, goal_cell, open, closed, counter, action_cost):
    while goal_cell.g > open.peek():
        curr_cell = tie_break(open)
        closed.add(curr_cell)
        neighbors = find_valid_neighbors(curr_cell, closed)
        #print(len(neighbors))
        for succ in neighbors:
            if succ.search < counter:
                succ.g = math.inf #Infinity
                succ.search = counter
            if succ.g > curr_cell.g + curr_cell.cost: #TODO: check
                succ.g = curr_cell.g + curr_cell.cost

                succ.pointer = curr_cell #Update tree pointer

                open.deleteItem(succ)

                succ.h = compute_h_value(succ)
                succ.f = succ.g + succ.h
                open.insert(succ)
    
    

def main():

    counter = 0
    action_cost = 1 #TODO: update this when needed

    start_x = m.agent_pos_x
    start_y = m.agent_pos_y
    start_cell = m.maze[start_x][start_y] # holds Cell object of current maze index
    goal_cell = m.maze[m.GOAL_X][m.GOAL_Y]  #holds Cell object of GOAL maze index

    while start_cell is not goal_cell:
        counter += 1

        start_cell.g = 0  # initial g value
        start_cell.search = counter
        goal_cell.g = math.inf # GOAl G value
        goal_cell.search = counter

        open = Heap() #TODO: Break ties properly
        closed = set() #set() = hashSet O(1) search

        start_cell.h = compute_h_value(start_cell)
        start_cell.f = start_cell.g + start_cell.h #f value
        open.insert(start_cell)
        
        compute_path(start_cell, goal_cell, open, closed, counter, action_cost)
        
        if open.size() == 0:
            print("Cannot reach Target!")
            return

        tree_pointer = goal_cell
        backtrack = [] #Saves the Cells the tree pointers follow, used to update Agent's location
        while tree_pointer is not start_cell is not None: #Follow pointers from goal -> start
            backtrack.append(tree_pointer)
            tree_pointer = tree_pointer.pointer
        
        backtrack.reverse() #Reverse list to follow it from start -> goal
        for cell in backtrack: #Update agent state until we hit a blocked cell
            if cell.is_blocked:
                action_cost += 1
                cell.cost += action_cost
                break
            #print([cell.x_pos, cell.y_pos])
            start_cell = cell
        #print([start_cell.x_pos, start_cell.y_pos])
    print("Target reached!")
    #print([start_cell.x_pos, start_cell.y_pos])
    #print([goal_cell.x_pos, goal_cell.y_pos])

def compute_h_value(cell):
    return abs(cell.x_pos - m.GOAL_X) + abs(cell.y_pos - m.GOAL_Y)


# adds all neighbors that havent been expanded yet (closed list)
def find_valid_neighbors(curr_cell, closed):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            row = curr_cell.x_pos
            col = curr_cell.y_pos
            if (i == 0 or j == 0) and i != j:
                row += i
                col += j
                #if (0 <= row < m.MAZE_SIZE and 0 <= col < m.MAZE_SIZE and not m.maze[row][col] in closed):
                if (row >= 0 and row < m.MAZE_SIZE and col >= 0 and col < m.MAZE_SIZE and not m.maze[row][col] in closed):
                    neighbors.append(m.maze[row][col])
    return neighbors
    
#This code in crazy
# Essentially tie breaks values with the same f values
# Selects based on SMALLEST g value
# if cells have the same G values, break tie RANDOMLY
def tie_break(open):
    min = open.delete()
    if open.size() == 0:
        return min
    
    f_list = []
    f_list.append(min)
    #print(open.size())
    while min.f == open.peek():
        f_list.append(open.delete())
        if (open.size() == 0):
            break

    min_g_cell = f_list[0]
    for cell in f_list:
        if min_g_cell.g > cell.g:
            min_g_cell = cell

    for cell in f_list:
        if cell.g != min_g_cell.g:
            open.insert(cell)
            f_list.remove(cell)

    retcell = random.choice(f_list)
    f_list.remove(retcell)

    for cell in f_list:
        open.insert(cell)
    #open.print()
    return retcell

