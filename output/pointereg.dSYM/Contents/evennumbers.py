"""
Step 1 : store all values in an array
Setp 2 : create a new array to store even numbers
Step 3 : check each value in the first array if it is even or not
Step 4 : if it is even then store it in the new array using append function
Step 5 : print the new array
"""

arr1 = [1, 2, 3, 4, 5,6,7,8,9,10]
arr2 = []
for value in arr1:
    if value % 2 ==0:
        arr2.append(value)
        
print(arr2)