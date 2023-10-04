#Lambda functions are also known as anonymous functions because they don't have a name like regular functions
add = lambda x : x+10
result = add(5)
print(result)

add2 = lambda m,n : n*m
value = add2(10,5)
print(value)

number = [2,3,4,5]
square = list(map(lambda x: x**2,number))
print(square)

def myfunc(x):
    return lambda x: x**2

double = myfunc(2)
tripple = myfunc(3)
print(double(10))
print(tripple(11))

