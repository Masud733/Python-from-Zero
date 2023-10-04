from itertools import groupby
code = "AAAADDDDHHHJKKKBBB"
grouped = groupby(code, key =None)
for key, group in grouped:
    print(f"key: {key} | group: {list(group)}")

# can also use groupby on other iterables
print("\n")

# from itertools import groupby
workers = [
    {'name': 'John', 'department': 'IT'},
    {'name': 'Masud', 'department': 'Data'},
    {'name': 'Avijit', 'department': 'IT'},
    {'name': 'Jasica', 'department': 'Design'},
    {'name': 'Jabir', 'department': 'Data'},
    {'name': 'Umair', 'department': 'Data'},
]

workers = sorted(workers, key=lambda d: d["department"])
grouped = groupby(workers, key=lambda d: d["department"])
for key1, group1 in grouped:
    print(f"key: {key1} | group: {list(group1)}")

