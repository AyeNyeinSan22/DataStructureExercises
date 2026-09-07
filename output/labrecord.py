usage = [45, 30, 60, 25, 50, 40, 35, 55]

#traverse the array and print the values
for value in usage:
    print(value)
    
#Finding the largest value without using max
copy_usage = usage.copy()
copy_usage.sort()
print("Largest value:", copy_usage[len(copy_usage)-1])

#Finding the smallest value without using min
print("Smallest value: ", copy_usage[0])

#asking user to enter a value to search in the array
search_value = int(input("Enter a value to search in the array:"))

#implementing a linear search to find the value
found = False
comparison_count = 0
for value in usage:
    comparison_count += 1
    if value == search_value:
        found = True
        break
    
    
#if the value is found, print the value with index no
if found: 
    print("Value found in the array: ", search_value, "at index:", usage.index(search_value))
else:
    print("Value not found.")
    
#Counting the comparison did in finding the value
print("Time complexity of the linear search :", comparison_count)

#state the time complexity of the transversing the array and performing the linear search
print("Time complexity of transversing the array : ", len(usage))



