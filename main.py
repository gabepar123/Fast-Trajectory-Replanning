from maze import *
from repeated_forward_astar import *
from reapeated_backwards_astar import *
from adaptive_astar import *
from maze_generator import *
import time


#TODO: visualize properly

def forward_vs_adaptive():

    total_time = 0
    total_cells_expanded = 0
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
    for i in range(50):
        aa = adaptive_astar(use_small_g=False, visualize=False, print_status=False, file_index=i)
        time, cells_expanded = aa.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Adaptive A*: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))

def forward_vs_backwards():
    
    total_time = 0
    total_cells_expanded = 0
    for i in range(50):
        rfa = repeated_forward_astar(use_small_g=False, visualize=False, print_status=False, file_index=i)
        time, cells_expanded = rfa.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Repeated Forward A*: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))
    
    total_time = 0
    total_cells_expanded = 0
    for i in range(50):
        rba = repeated_backwards_astar(use_small_g=False, visualize=False, print_status=False, file_index=i)
        time, cells_expanded = rba.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Repeated Backwards A*: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))


def small_vs_large():

    total_time = 0
    total_cells_expanded = 0
    for i in range(50):
        rla = repeated_forward_astar(use_small_g=False, visualize=False, print_status=False, file_index=i)
        time, cells_expanded = rla.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Repeated Forward A*: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))

    total_time = 0
    total_cells_expanded = 0
    for i in range(50):
        rsa = repeated_forward_astar(use_small_g=True, visualize=False, print_status=False, file_index=i)
        time, cells_expanded = rsa.run()
        total_time += time
        total_cells_expanded += cells_expanded
    avg_time = total_time / 50
    avg_cells_expanded = cells_expanded / 50
    print("Repeated Forward A*: Average Total time: %f; Average Cells Expanded: %f" % (avg_time, avg_cells_expanded))


#Code for generating grid worlds
#Creating 50 grid worlds
    #for i in range(0, 50):
    #    maze_gen = Maze_Gen()
    #    maze_gen.generate_maze()
    #    maze_gen.create_maze_file(i)


if __name__ == '__main__':

    while True:
        user_input = input("""1) Visualize Repeated Forward A*      2) Visualize Adaptive A*\n
3) Visualize Backwards Repeated A*    4) Compare Repeated Forward A* vs Adaptive A*\n
5) Compare Repeated Forward A* vs Repeated Backwards A* (WARNING: Takes up to 6 minutes)\n
6) Compare Smaller G Value vs Bigger G Value (WARNING: Takes up to 6 minutes)\n
7) Quit\n """)
        
        if user_input == '1':
            rfa = repeated_forward_astar(use_small_g=False, visualize=True, print_status=True, file_index=1) #TODO: get nice grid world
            rfa.run()
            
        elif user_input == '2':
            aa = adaptive_astar(use_small_g=False, visualize=True, print_status=True, file_index=1) #TODO: get nice grid world
            aa.run()
        
        elif user_input == '3':
            rba = repeated_backwards_astar(use_small_g=False, visualize=True, print_status=True, file_index=1) #TODO: get nice grid world
            rba.run()

        elif user_input == '4':
            forward_vs_adaptive()
        elif user_input == '5':
            forward_vs_backwards()
        elif user_input == '6':
            small_vs_large()
        elif user_input == '7':
            break
        else:
            print("Invalid Input!")
        print("\n")