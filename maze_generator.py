import random

class Maze_Gen:

    def __init__(self):
        self.MAZE_SIZE = 101
        self.maze = [["x" for j in range(self.MAZE_SIZE)] for i in range(self.MAZE_SIZE)]
        self.agent_pos_x = 0
        self.agent_pos_y = 0
        self.goal_x = 100
        self.goal_y = 100

    def generate_maze(self):

        list = []
        list.append([self.agent_pos_x,self.agent_pos_y,self.agent_pos_x,self.agent_pos_y])

        while len(list) != 0:
            c = random.choice(list)
            list.remove(c)
            x = c[2]
            y = c[3]

            if (self.maze[x][y] == "x"):
                self.maze[c[0]][c[1]] = "-"
                self.maze[x][y] = "-"

                if x >= 2 and self.maze[x-2][y] == "x":
                    list.append([x-1, y, x-2, y])
                if y >= 2 and self.maze[x][y-2] == "x":
                    list.append([x, y-1, x, y-2])
                if x < self.MAZE_SIZE - 2 and self.maze[x+2][y] == "x":
                    list.append([x+1, y, x+2, y])
                if y < self.MAZE_SIZE - 2 and self.maze[x][y+2] == "x":
                    list.append([x, y+1, x, y+2])
            
            self.goal_x = x
            self.goal_y = y

        for i, row in enumerate(self.maze):
            for j, col in enumerate(row):
                rand = random.random()
                if self.maze[i][j] == "x" and rand < 0.25:
                    self.maze[i][j] = "-"

        self.maze[self.goal_x][self.goal_y] = "G"
        self.maze[self.agent_pos_x][self.agent_pos_y] = "A"

    def print_maze(self):
        for row in self.maze:
            print("", end ="")
            for col in row:
                print(col, end = "")
            print("")

    def create_maze_file(self, index):
        file_name = "grid_worlds/" + str(index) + ".txt"
        f = open(file_name, "w")
        for row in self.maze:
            for cell in row:
                f.write(cell)
            f.write("\n")
        f.write(str(self.goal_x) + " " + str(self.goal_y))
        f.close()
