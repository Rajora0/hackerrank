def compareTriplets(a, b):
    """
    Compare corresponding elements of two lists and count how many times
    elements in the first list are greater than, or less than elements in the second list.

    Args:
        a (list of int): The first list of integers.
        b (list of int): The second list of integers.

    Returns:
        list of int: A list with two integers:
                    - The first integer is the count of elements in `a` greater than corresponding elements in `b`.
                    - The second integer is the count of elements in `a` less than corresponding elements in `b`.
    """
    n1 = 0  # Initialize count for elements in `a` greater than those in `b`
    n2 = 0  # Initialize count for elements in `a` less than those in `b`
    
    # Iterate through pairs of elements from `a` and `b`
    for i, k in zip(a, b):
        if i > k:
            n1 += 1  # Increment count for elements in `a` greater than `b`
        elif i < k:
            n2 += 1  # Increment count for elements in `a` less than `b`
    
    # Return the counts as a list
    return [n1, n2]


# Example usage
a = [1, 2, 3]
b = [3, 2, 1]

# Call the function with example lists and print the result
res = compareTriplets(a, b)
print(res)  # Output: [1, 1]
