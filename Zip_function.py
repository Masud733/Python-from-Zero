# Creating two lists
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Using zip to pair elements from both lists
zipped_data = zip(names, scores)
print("Zipping two list together:",zipped_data)

# Converting the zip object to a list of tuples
zipped_list = list(zipped_data)
print("Converting the zip to a list of tuples:",zipped_list)

# Output:
# [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
