# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
tuple = ("banana","cherry","Mango")
iterator = iter(tuple)
print(next(iterator))
print(next(iterator))
print(next(iterator))

mystr = "Banana"
iter = iter(mystr)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Using the custom iterator
my_iter = MyIterator(0, 5)

for num in my_iter:
    print(num)

#write a program about string iterator
class stringIniterator:
    def __init__(self,input_string):
        self.input_string = input_string
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.input_string):
            result = self.input_string[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_string = "Hello World"
my_iterator = stringIniterator(my_string)

for char in my_iterator:
    print(char)

