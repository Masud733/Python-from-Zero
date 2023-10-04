arr_list = [33, "Masud",3.5, [1,2,3],"Python"]
print(arr_list[1])
print("Python"in arr_list)

for item in arr_list:
    if 44 in arr_list:
        print("Element is the list.")
    else:
        print("Not is the list")
for item in arr_list:
    if isinstance(item, str):
        print(f"{item} is a string")
    else:
        print(f"{item} is not a string")
