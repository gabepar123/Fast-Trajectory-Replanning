from maze import *
from repeated_forward_astar import *
from reapeated_backwards_astar import *
from adaptive_astar import *
from maze_generator import *
import time


#Creating 50 grid worlds
    #for i in range(0, 50):
    #    maze_gen = Maze_Gen()
    #    maze_gen.generate_maze()
    #    maze_gen.create_maze_file(i)
#TODO: visualize properly

if __name__ == '__main__':

    #Creating 50 grid worlds
    #for i in range(0, 50):
    #    maze_gen = Maze_Gen()
    #    maze_gen.generate_maze()
    #    maze_gen.create_maze_file(i)
    
    total_time = 0
    total_cells_expanded = 0
    time = 0
    cells_expanded = 0
    
    for i in range(50):
        rfa = repeated_forward_astar(use_small_g=False, visualize=False, print_status=False, file_index=i)
        time, cells_expanded = rfa.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Repeated FORWARD A*: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))


    total_time = 0
    total_cells_expanded = 0
    time = 0
    cells_expanded = 0
    
    for i in range(50):
        aa = adaptive_astar(use_small_g=False, visualize=False, print_status=False, file_index=i)
        time, cells_expanded = aa.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Adaptive A*: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))


    #total_time = 0
    #total_cells_expanded = 0
    #time = 0
    #cells_expanded = 0
    #
    #for i in range(50):
    #    rsa = repeated_forward_astar(use_small_g=True, visualize=False, print_status=False, file_index=i)
    #    time, cells_expanded = rsa.run()
    #    total_time += time
    #    total_cells_expanded += cells_expanded
    #avg_time = total_time / 50
    #avg_cells_expanded = cells_expanded / 50
    #print("Repeated Forward A* using Smaller G values: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))
#
#
    #total_time = 0
    #total_cells_expanded = 0
    #time = 0
    #cells_expanded = 0
    #
    #for i in range(50):
    #    rba = repeated_backwards_astar(use_small_g=False, visualize=False, print_status=False, file_index=i)
    #    time, cells_expanded = rba.run()
    #    total_time += time
    #    total_cells_expanded += cells_expanded
    #avg_time = total_time / 50
    #avg_cells_expanded = cells_expanded / 50
    #print("Repeated Backwards A*: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))
#