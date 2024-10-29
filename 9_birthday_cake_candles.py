def birthdayCakeCandles(candles):
    """
    Calculate the number of candles on a birthday cake that are the tallest.

    Args:
        candles (list): A list of integers representing the heights of the candles.

    Returns:
        int: The number of candles that have the maximum height.
    """
    # Find the maximum height among the candles
    MAX = max(candles)

    # Initialize a counter to keep track of how many candles have the maximum height
    COUNT = 0

    # Loop through the candles to count how many have the maximum height
    for i in candles:
        if i == MAX:
            COUNT += 1
        
    # Return the count of the tallest candles
    return COUNT

# Example usage
candles = [4, 4, 1, 3]
print(birthdayCakeCandles(candles))
