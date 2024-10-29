def miniMaxSum(arr):
    """
    Calculate and print the minimum and maximum sums of an array of integers.
    
    The function considers the four smallest elements for the minimum sum 
    and the four largest elements for the maximum sum.

    Args:
        arr (list): A list of five integers.

    Returns:
        None
    """
    # Sort the array in ascending order
    arr_sorted = sorted(arr)

    # Calculate the minimum sum using the first four elements of the sorted list
    min_sum = sum(arr_sorted[:4])

    # Calculate the maximum sum using the last four elements of the sorted list
    max_sum = sum(arr_sorted[1:])

    # Print the minimum sum and maximum sum
    print(f'{min_sum} {max_sum}')

# Example usage
arr = [1, 3, 5, 7, 9]
miniMaxSum(arr)