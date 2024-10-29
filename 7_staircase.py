# def staircase(n):
#     """
#     Print a staircase of height `n` using the character `#`.
#     Each line represents a level of the staircase, right-aligned.

#     Args:
#         n (int): The height of the staircase.

#     Returns:
#         None
#     """
#     # Loop through each level of the staircase
#     for i in range(n):
#         # Calculate the number of spaces and hashes for the current level
#         spaces = (n - (i + 1)) * ' '  # Right-align the hashes
#         hashes = ((n + 1) - (n - i)) * '#'  # Incremental number of hashes

#         # Print the current level of the staircase
#         print(spaces + hashes)

# # Example usage
# staircase(6)

# def staircase(n):
#     """
#     Print a staircase of height `n` using the character `#`.
#     Each line represents a level of the staircase, right-aligned.

#     Args:
#         n (int): The height of the staircase.

#     Returns:
#         None
#     """
#     # Loop through each level of the staircase and directly format the string
#     for i in range(1, n + 1):
#         print(f"{' ' * (n - i)}{'#' * i}")

# # Example usage
# staircase(6)


def staircase(n):
    """
    Print a staircase of height `n` using the character `#`.
    Each line represents a level of the staircase, right-aligned.

    Args:
        n (int): The height of the staircase.

    Returns:
        None
    """
    for i in range(1, n + 1):
        print(('#' * i).rjust(n))

# Example usage
staircase(6)
