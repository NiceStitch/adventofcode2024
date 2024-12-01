# Create two lists 
with open('input.txt', 'r') as file:
    left_column = []
    right_column = []
    
    for line in file:
        left, right = map(int, line.split())
        left_column.append(left)
        right_column.append(right)

# Sort the two lists 

left_column.sort()
right_column.sort()

# Loop through lists 
count = 0
for i in range(len(left_column)):
    diff = abs(left_column[i] - right_column[i])
    count += diff
print(count)

# Part 2
occur = 0
for id in left_column:
    occur += id * right_column.count(id)
print(occur)