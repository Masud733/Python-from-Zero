fruits = ["Rose apple","Date","Cherry","Kiwi","Tamarind"]
#accessing elements
print("First fruit: ",fruits[0])
print("Last fruit: ",fruits[4])
print("Fruits are: ", fruits)
#replace fruit
fruits[2] = "Rambutan"
print("Modified fruits: ",fruits)
#add fruit
fruits.append("Avocado")
print("Fruits after appended: ",fruits)

#Tuple type
print("\n")
colors = ["purple","lavender","black"]
print("Last color: ",colors[2])
#unpack a tuple
color0, color1, color2 = colors
print("Unpack the colors: ",color0, color1, color2)

# Creating a range with a specified start, end, and step
stepped_range = range(1,100,5)  # Generates numbers from 1 to 100 with a step of 5

# Iterating over the stepped range
print("Using a for loop with stepped range:")
for num in stepped_range:
    print(num)





