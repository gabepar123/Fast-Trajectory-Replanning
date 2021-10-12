from binary_heap import *
from maze import *
import math

m = Maze()
m.create_maze_dfs()
m.print_maze()

found_blocked = False #used for tracing tree pointers
start_cell = None
action_cost = 1

def compute_path(start_cell, goal_cell, open, closed, counter, action_cost):
    while goal_cell.g > open.peek():
        curr_cell = open.delete()
        closed.add(curr_cell)
        neighbors = find_valid_neighbors(curr_cell, closed)
        for succ in neighbors:
            if succ.search < counter:
                succ.g = math.inf #Infinity
                succ.search = counter
            if succ.g > curr_cell.g + action_cost: #TODO: check
                succ.g = curr_cell.g + action_cost

                succ.pointer = curr_cell #Update tree pointer

                succ.h = compute_h_value(succ)
                succ.f = succ.g + succ.h
                open.deleteItem(succ)
                open.insert(succ)
    
    

def main():
    global found_blocked
    global start_cell
    global action_cost #TODO: update this when needed

    counter = 0

    start_x = m.agent_pos_x
    start_y = m.agent_pos_y
    start_cell = m.maze[start_x][start_y] # holds Cell object of current maze index
    goal_cell = m.maze[m.GOAL_X][m.GOAL_Y]  #holds Cell object of GOAL maze index

    while start_cell != goal_cell:
        print("here")
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

        
        backtrack_tree_pointer(goal_cell) #Follow pointers from goal -> start
        #tree pointers
        #set start state
        #update cost
    print("Target reached!")
    print([start_cell.x_pos, start_cell.y_pos])
    print([goal_cell.x_pos, goal_cell.y_pos])

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
    
    #TODO: this function is probably off by one
def backtrack_tree_pointer(p):
    global found_blocked
    global start_cell
    global action_cost

    if p == None or found_blocked:
        return

    backtrack_tree_pointer(p.pointer)

    if p.is_blocked:
        found_blocked = True
        action_cost += 1
        return
    start_cell = p
    

