# START
#     values = [7, 12,9, 4,11]
#     lowest = values[0]

#     FOR each value in values
#         IF value < lowest
#             lowest = value
#         END IF
#     END FOR

#     PRINT lowest
# END

# Step 1: Start

# Step 2: Store the values in an array.

# values = [7, 12, 9 , 4, 11}]

# Step 3: Set the first value as the lowest value.

# lowest = 7

# Step 4: Compare each value with lowest.

# Step 5: If the current value is smaller than lowest, set the current value as the new lowest.

# Step 6: Repeat Steps 4–5 until all values have been checked.

# Step 7: Display the lowest value.

# Step 8: Stop.

array = [7,12,9,4,11];
lowest = array[0];

for value in array:
    if value < lowest:
        lowest = value;
        
print(lowest)