
countries ={"USA","UK","Australia","Germany"}
countries.add("France")
print("The countries are:",countries)
countries.remove("Germany")
print("after removing one:",countries)

for country in countries:
    print(country)
print("Total countries:",len(countries))
print("USA" in countries)
print("Bangladesh" in countries)



#set operations
set1 = {1,2,3,4,5}
set2 = {5,6,7,8}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print("\n")
print("Union of this set:",union_set)
print("Intersection of this set:",intersection_set)
print("Difference of this set:",difference_set)
