from FireForest import FireForest

if __name__ == "__main__":
    forest_x, forest_y = 10, 10
    burn_time = 3
    spreading_chance = 10
    fireForest = FireForest(forest_x, forest_y, burn_time, spreading_chance)
    fireForest.simulation()

