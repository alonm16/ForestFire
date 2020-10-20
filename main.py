from FireForest import FireForest


def main():
    """
    gets user input and start the simulation
    """
    while True:
        forest_x, forest_y = [int(dimension) for dimension in input("Enter Forest Dimensions: ").split()]
        burn_time = int(input("Enter Tree Burn Time: "))
        spreading_probability = int(input("Enter Probability of Fire to Spread: "))
        # forest_x, forest_y = 40, 40
        # burn_time = 3
        # spreading_chance = 10
        FireForest(forest_x, forest_y, burn_time, spreading_probability).simulation()

        if input("Would you like to try again? (y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    main()
