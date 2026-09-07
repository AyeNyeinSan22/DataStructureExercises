
"""
Step 1 : store all values in an array
Step 2 : sort the array in ascending order from the lowest to the highest
Step 3 : print the last value in the array which is the largest number
"""

arr = [1, 4, 7, 1, 10, 11, 2]
arr.sort() # [1, 1, 2, 4, 7, 10, 11]
print(arr[len(arr)-1]) # arr[7-1] = arr[6] = 11