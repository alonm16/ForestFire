import random


class FireTree:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.time = FireForest.burn_time

    def decrease_time(self):
        self.time = self.time-1


class FireForest:
    burn_time = 0

    def __init__(self, forest_x, forest_y, burn_time, spreading_chance):
        FireForest.burn_time = burn_time
        self.forest_x = forest_x
        self.forest_y = forest_y
        self.spreading_chance = spreading_chance
        self.forest_arr = None
        self.on_fire_arr = None

    def __get_legal_neighbors(self, row, col):
        neighbors = [(row, col+1), (row, col-1), (row+1, col), (row+1, col+1), (row+1, col-1), (row-1, col),
                     (row-1, col+1), (row-1, col-1)]
        return [(x, y) for (x, y) in neighbors if 0 <= x <= self.forest_x and 0 <= y <= self.forest_y]

    def __step(self):
        for i in range(len(self.on_fire_arr)):
            curr_tree = self.on_fire_arr.pop(0)
            for (neighbor_row, neighbor_col) in self.__get_legal_neighbors(curr_tree.row, curr_tree.col):
                if random.randint(1, 100) <= self.spreading_chance:
                    self.forest_arr[neighbor_row][neighbor_col] = True
                    self.on_fire_arr.append(FireTree(neighbor_row, neighbor_col))

            curr_tree.decrease_time()
            if curr_tree.time > 0:
                self.on_fire_arr.append(curr_tree)

    def simulation(self):
        self.forest_arr = [[False for _ in range(self.forest_y)] for _ in range(self.forest_x)]
        start_tree_x = random.randint(self.forest_x)
        start_tree_y = random.randint(self.forest_y)
        self.forest_arr[start_tree_x][start_tree_y] = True
        self.on_fire_arr = [FireTree(start_tree_x, start_tree_y)]
        while len(self.on_fire_arr) > 0:
            self.__step()






