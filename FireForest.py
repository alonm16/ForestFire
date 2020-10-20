import random


class FireTree:
    burn_time = 0

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.time = FireTree.burn_time

    def decrease_time(self):
        self.time = self.time-1


class FireForest:

    def __init__(self, forest_x, forest_y, burn_time, spreading_chance):
        FireTree.burn_time = burn_time
        self.forest_x = forest_x
        self.forest_y = forest_y
        self.spreading_chance = spreading_chance
        self.forest_arr = [[False for _ in range(self.forest_y)] for _ in range(self.forest_x)]
        self.on_fire_arr = []
        self.time = 0
        self.number_burned_trees = 1

    def __get_legal_neighbors(self, row, col):
        neighbors = [(row, col+1), (row, col-1), (row+1, col), (row+1, col+1), (row+1, col-1), (row-1, col),
                     (row-1, col+1), (row-1, col-1)]
        return [(x, y) for (x, y) in neighbors if 0 <= x < self.forest_x and 0 <= y < self.forest_y]

    def __step(self):
        for i in range(len(self.on_fire_arr)):
            curr_tree = self.on_fire_arr.pop(0)
            for (neighbor_row, neighbor_col) in self.__get_legal_neighbors(curr_tree.row, curr_tree.col):
                if random.randint(1, 100) <= self.spreading_chance and not self.forest_arr[neighbor_row][neighbor_col]:
                    self.forest_arr[neighbor_row][neighbor_col] = True
                    self.on_fire_arr.append(FireTree(neighbor_row, neighbor_col))
                    self.number_burned_trees += 1

            curr_tree.decrease_time()
            if curr_tree.time > 0:
                self.on_fire_arr.append(curr_tree)

    def conclusion(self):
        total_trees = self.forest_x * self.forest_y
        alive_trees = total_trees - self.number_burned_trees
        survival_rate = alive_trees/total_trees
        print("Total Time : " + str(self.time))
        print("Total Trees: " + str(total_trees))
        print("Burned Trees: " + str(self.number_burned_trees))
        print("Non Burned Trees: " + str(alive_trees))
        print("Survival Rate: " + str(survival_rate))

    def simulation(self):
        start_tree_x = random.randint(0, self.forest_x-1)
        start_tree_y = random.randint(0, self.forest_y-1)
        self.forest_arr[start_tree_x][start_tree_y] = True
        self.on_fire_arr = [FireTree(start_tree_x, start_tree_y)]
        while len(self.on_fire_arr) > 0:
            self.__step()
            self.time += 1

        self.conclusion()






