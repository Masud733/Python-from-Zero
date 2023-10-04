#Local scop
#The local variable can be accessed from a function within the function:
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()

#Global scop
#A variable created outside of a function is global and can be used by anyone
y = 5000
def myfunction():
    print(y)
myfunction()
print(y)
#use the global keyword if you want to make a change to a global variable inside a function.
z = 1000
def globalfunc():
    global z
    z = 2000
globalfunc()
print(z)


