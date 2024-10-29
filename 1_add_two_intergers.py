def solveMeFirst(a, b):
    """
    This function sums two integers.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
        
    Returns:
        int: The sum of the two integers.
    """
    return a + b
    
# Read the first integer from user input and convert it to an integer
num1 = int(input())

# Read the second integer from user input and convert it to an integer
num2 = int(input())

# Call the function solveMeFirst with num1 and num2 as arguments, and store the result in 'res'
res = solveMeFirst(num1, num2)

# Print the result of the function call
print(res)
