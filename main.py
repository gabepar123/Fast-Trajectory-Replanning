from maze import *
from repeated_forward_astar import *
import time



#rfa = repeated_forward_astar(True)
#time, cells_expanded = rfa.run()


if __name__ == '__main__':
    total_time = 0
    total_cells_expanded = 0
    
    for i in range(50):
        rfa = repeated_forward_astar(use_small_g=False)
        time, cells_expanded = rfa.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Using Larger G Value: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))



    total_time = 0
    total_cells_expanded = 0
    for i in range(50):
        rfa = repeated_forward_astar(use_small_g=True)
        #rfa.m.print_maze()
        time, cells_expanded = rfa.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Using Smaller G Value: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))




