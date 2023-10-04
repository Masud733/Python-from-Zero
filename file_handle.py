

# file = open("Text_py.txt","a")
# file.write("\nThe python is burning my mind Im awake for that!")
# file.close()
# file = open("Text_py.txt","r")
# print(file.read())
# file.close
# Check if the message is already in the file
message = "\nThe python is burning my mind Im awake for that!"
with open("Text_py.txt", "r") as file:
    file_content = file.read()

if message not in file_content:
    # Append the message to the file if it's not already present
    with open("Text_py.txt", "a") as file:
        file.write("\n" + message)

# Read and print the file's content
with open("Text_py.txt", "r") as file:
    print(file.read())



