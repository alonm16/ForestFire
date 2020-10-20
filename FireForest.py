import random
import matplotlib.colors as colors
import matplotlib.pyplot as plt
import time


class FireTree:
    burn_time = 0

    def __init__(self, row, col):
        """
        :param row: row position of the tree in the forest matrix
        :param col: col position of the tree in the forest matrix
        """
        self.row = row
        self.col = col
        self.time_to_burn = FireTree.burn_time

    def decrease_time(self):
        self.time_to_burn = self.time_to_burn-1


class FireForest:

    def __init__(self, forest_x, forest_y, burn_time, spreading_probability):
        """
        forest_mat: matrix representing the forest by 1 meaning
                      the tree has been burned and 0 meaning it wasn't
        on_fire: list of trees that are currently on fire
        :param forest_x: number of rows in the matrix
        :param forest_y: number of columns in the matrix
        :param burn_time: the time it takes a tree to burn
        :param spreading_probability: probability of fire to spread between trees
        """
        FireTree.burn_time = burn_time
        self.forest_x = forest_x
        self.forest_y = forest_y
        self.spreading_probability = spreading_probability
        self.forest_mat = [[0 for _ in range(self.forest_y)] for _ in range(self.forest_x)]
        self.on_fire = []
        self.time = 0
        self.number_burned_trees = 1

    def __get_legal_neighbors(self, row, col):
        neighbors = [(row, col+1), (row, col-1), (row+1, col), (row+1, col+1), (row+1, col-1), (row-1, col),
                     (row-1, col+1), (row-1, col-1)]
        return [(x, y) for (x, y) in neighbors if 0 <= x < self.forest_x and 0 <= y < self.forest_y]

    def __step(self):
        """
        for each burning tree, neighboring trees might get burned according to the spreading probability
        """
        for i in range(len(self.on_fire)):
            curr_tree = self.on_fire.pop(0)
            for (neighbor_row, neighbor_col) in self.__get_legal_neighbors(curr_tree.row, curr_tree.col):
                if random.randint(1, 100) <= self.spreading_probability and\
                        not self.forest_mat[neighbor_row][neighbor_col]:
                    self.forest_mat[neighbor_row][neighbor_col] = 1
                    self.on_fire.append(FireTree(neighbor_row, neighbor_col))
                    self.number_burned_trees += 1

            curr_tree.decrease_time()
            if curr_tree.time_to_burn > 0:
                self.on_fire.append(curr_tree)

    def print_forest(self):
        cmap = colors.ListedColormap(["green", "red"])
        plt.title('burning forest time ' + str(self.time))
        plt.imshow(self.forest_mat, cmap=cmap)
        plt.show()
        time.sleep(0.05)

    def conclusion(self):
        total_trees = self.forest_x * self.forest_y
        alive_trees = total_trees - self.number_burned_trees
        survival_rate = alive_trees/total_trees
        print("\nResults:")
        print("Total Time : " + str(self.time))
        print("Total Trees: " + str(total_trees))
        print("Burned Trees: " + str(self.number_burned_trees))
        print("Non Burned Trees: " + str(alive_trees))
        print("Survival Rate: " + str(survival_rate) + "\n")

    def simulation(self):
        """
        picks a tree randomly that starts to burn, and run each step until the forest stops to burn
        """
        start_tree_x = random.randint(0, self.forest_x-1)
        start_tree_y = random.randint(0, self.forest_y-1)
        self.forest_mat[start_tree_x][start_tree_y] = 1
        self.on_fire = [FireTree(start_tree_x, start_tree_y)]
        while len(self.on_fire) > 0:
            self.__step()
            self.time += 1
            self.print_forest()

        self.conclusion()

