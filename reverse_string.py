def reverse_string(input_string):
    """Reverses a given string.

    Args:
      input_string: The string to be reversed.

    Returns:
      The reversed string.
    """
    return input_string[::-1]

# Get input from the user
user_string = input("Enter a string: ")

# Reverse the string
reversed_string = reverse_string(user_string)

# Print the reversed string
print("Reversed string:", reversed_string)