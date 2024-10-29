def simple_sum(iterable, start=0):
    """
    This function sums up all elements in an iterable, starting from an initial value.
    
    Args:
        iterable (iterable): An iterable (like a list) containing numbers to be summed.
        start (int): An initial value to start the sum with (default is 0).
        
    Returns:
        int: The sum of the elements in the iterable plus the start value.
    """
    total = start  # Initialize total with the start value
    for item in iterable:  # Iterate over each item in the iterable
        total += item  # Add each item to the total
    return total  # Return the final sum


def simpleArraySum(ar):
    """
    This function calculates the sum of an array of integers using the simple_sum function.
    
    Args:
        ar (list of int): A list of integers to be summed.
        
    Returns:
        int: The sum of the integers in the array.
    """
    return simple_sum(ar, start=0)  # Call simple_sum with the array and a start value of 0


# Example usage
res = simpleArraySum([1, 2, 3, 4, 5])
print(res)  # Output the result of the sum (15)
