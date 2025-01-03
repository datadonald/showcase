# Questions:

# 1.            Find Cost of Tile to Cover W x H Floor –

# Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
# 2.            Find max combination of 2 numbers in a sequence - n^2

# 3.            Write some code that simulates flipping a single coin however many times the user decides. The code should record the outcomes and count the number of tails and heads.

# 4.            Enter a string and the program will reverse it and print it out.

# 5.            Reads a file of records, sorts them, and then writes them back to the file. Allow the user to choose various sort style and sorting based on a particular field.

import random

def coin_flip_simulator():
    """Simulates flipping a coin a user-specified number of times."""

    try:
        num_flips = int(input("How many times would you like to flip the coin? "))
        if num_flips <= 0:
            print("Please enter a positive number of flips.")
            return  # Exit the function if input is invalid
    except ValueError:
        print("Invalid input. Please enter a number.")
        return #Exit function if input is not a number

    outcomes = []
    heads_count = 0
    tails_count = 0

    for _ in range(num_flips):
        flip = random.choice(["Heads", "Tails"])
        outcomes.append(flip)

        if flip == "Heads":
            heads_count += 1
        else:
            tails_count += 1

    print("\nResults:")
    print("-------")
    for i, outcome in enumerate(outcomes):
        print(f"Flip {i+1}: {outcome}")

    print("\nSummary:")
    print(f"Total Heads: {heads_count}")
    print(f"Total Tails: {tails_count}")
    print(f"Total Flips: {len(outcomes)}")

    head_percentage = (heads_count / len(outcomes)) * 100
    tail_percentage = (tails_count / len(outcomes)) * 100

    print(f"Percentage of Heads: {head_percentage:.2f}%")
    print(f"Percentage of Tails: {tail_percentage:.2f}%")

if __name__ == "__main__":
    coin_flip_simulator()