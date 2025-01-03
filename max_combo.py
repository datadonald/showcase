def max_combination_n2(sequence):
    """
    Finds the maximum sum of any two numbers in a sequence using an O(n^2) approach.

    Args:
        sequence: A list or tuple of numbers.

    Returns:
        A tuple containing:
        - The maximum sum found (or None if the sequence has fewer than 2 elements).
        - The two numbers that produce the maximum sum (or None, None if not found).
    """

    if not sequence or len(sequence) < 2:  # Check for empty or too short sequences
        return None, None, None

    max_sum = float('-inf')  # Initialize with negative infinity
    num1 = None
    num2 = None

    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):  # Avoid comparing a number with itself
            current_sum = sequence[i] + sequence[j]
            if current_sum > max_sum:
                max_sum = current_sum
                num1 = sequence[i]
                num2 = sequence[j]

    return max_sum, num1, num2

# Example Usage and Testing
test_cases = [
    [1, 5, 2, 8, 3, 9, 4],  # Standard case
    [-1, -5, -2, -8, -3, -9, -4], #All negative numbers
    [1, 1, 1, 1, 1], #All same numbers
    [1, 2],         # Minimum valid case
    [1],            # Single element
    [],             # Empty list
    [5, -10, 15, -5] #Mix of positive and negative
]

for sequence in test_cases:
    max_sum, n1, n2 = max_combination_n2(sequence)
    if max_sum is not None:
        print(f"Sequence: {sequence}")
        print(f"Max sum: {max_sum} (from {n1} and {n2})\n")
    else:
        print(f"Sequence: {sequence}")
        print("Not enough numbers in sequence to find a combination.\n")
        
