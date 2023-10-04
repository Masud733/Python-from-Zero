x = "Masud Mehrab"
print(x.upper())
print(x.lower())
print(x.split(","))
print(x.replace("M","K"))
print(x.encode())

price = 5000
cgpa = 3.5
quality = 100000
able = "You will fight with {} student for ${} per annum scholarship with {} cgpa!"
print(able.format(quality,price,cgpa))
# name inside the curly brackets
myorder = "I have {car} that going {dis} km with just per litter fuel. Asking price ${price:.2f}."
print(myorder.format(car = "Mazda MX",dis = 15,price = 2000))
