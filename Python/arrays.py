import numpy as np

# Create the array
array = np.arange(10, 34).reshape(8, 3)

# Split the array into 4 equal parts
part1, part2, part3, part4 = np.array_split(array, 4)

# Print the 4 parts
print("Part 1:")
print(part1)
print("\nPart 2:")
print(part2)
print("\nPart 3:")
print(part3)
print("\nPart 4:")
print(part4)
