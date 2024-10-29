def aVeryBigSum(ar):
    """
    This function calculates the sum of a list of large integers.
    
    Args:
        ar (list of int): A list of integers to be summed.
        
    Returns:
        int: The sum of all integers in the list.
    """
    return sum(ar)  # Use the built-in sum function to calculate the total

# Example usage
res = aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005])
print(res)  # Output the result of the sum
