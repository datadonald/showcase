def calculate_tile_cost():
    """Calculates the total cost of tiling a floor."""

    try:
        width = float(input("Enter the width of the floor (in feet): "))
        height = float(input("Enter the height of the floor (in feet): "))
        tile_cost_per_sq_ft = float(input("Enter the cost of tile per square foot: "))

        if width <= 0 or height <= 0 or tile_cost_per_sq_ft <= 0:
            raise ValueError("Dimensions and cost must be positive values.")

    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    area = width * height
    total_cost = area * tile_cost_per_sq_ft

    print(f"\nThe area of the floor is: {area:.2f} square feet.")
    print(f"The total cost of tiling the floor is: ${total_cost:.2f}")

if __name__ == "__main__":
    calculate_tile_cost()
    