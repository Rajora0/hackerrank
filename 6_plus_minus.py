def plusMinus(arr):
    """
    Calculate and return the proportions of positive, negative, and zero values
    in a list of integers, formatted to six decimal places.

    Args:
        arr (list of int): A list of integers.

    Returns:
        tuple: Proportions of positive, negative, and zero values.
    """
    l = len(arr)  # Length of the list

    # Initialize counters
    positives, negatives, zeros = 0, 0, 0

    # Count occurrences
    for x in arr:
        if x > 0:
            positives += 1
        elif x < 0:
            negatives += 1
        else:
            zeros += 1
    
    # Return proportions formatted to six decimal places
    return (positives / l, negatives / l, zeros / l)

# Example usage
arr = [1, 1, 0, -1, -1]
positives, negatives, zeros = plusMinus(arr)
print(f"{positives:.6f}")
print(f"{negatives:.6f}")
print(f"{zeros:.6f}")
