import random

MAZE_SIZE = 101
maze = [["█"]*MAZE_SIZE for i in range(MAZE_SIZE)]




def print_maze():
    for row in maze:
        print("[", end ="")
        for col in row:
            print(col, end = "")
        print("]")

#
# Creates grid world using stack DFS
# Marking the index as "-" corresponds to UNBLOCKED
# Marking the index as "x" corresponds to BLOCKED
#
def create_maze_dfs():
    global maze
    visited = [[False]*MAZE_SIZE for _ in range(MAZE_SIZE)]

    row = start_row = random.randint(0, MAZE_SIZE - 1)
    row = start_col = random.randint(0, MAZE_SIZE - 1)

    st = []
    st.append([start_row, start_col])

    while (len(st) > 0):
        curr = st.pop()
        row = curr[0]
        col = curr[1]
        
        if (row < 0 or row >= MAZE_SIZE or col < 0 or col >= MAZE_SIZE or visited[row][col]):
            continue
        
        visited[row][col] = True

        rand = random.random()
        # we mark an index as unblocked 70% of the time
        # or if it is the first index
        if rand < 0.7 or (row == start_row and col == start_col) :
            maze[row][col] = "-"
            #we only add unblocked indexs to the stack
            
        else:
            maze[row][col] = "█"

        st.append([row + 1, col])
        st.append([row - 1, col])
        st.append([row, col + 1])
        st.append([row, col - 1])


def create_maze_backtracking():
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

create_maze_backtracking()
print_maze()