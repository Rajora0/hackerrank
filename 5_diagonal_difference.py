def diagonalDifference(arr):


    d1 = 0
    d2 = 0

    for i, arr in enumerate(arr):
        
        d1 += arr[i]
        d2 += arr[-i-1]
        
    return abs(d1-d2)
    

arr = [[1, 2, 3],[4, 5, 6], [9, 8 ,9]]

res = diagonalDifference(arr)

# Print the result of the function call
print(res)








