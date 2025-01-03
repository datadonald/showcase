import random

def coin_flip_sim():
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
    coin_flip_sim()