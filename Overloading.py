#define multiple methods with the same name in a class, but with different parameters. 
class Calculator:
    def add(self, *args):
        if len(args) == 2:
            return args[0] + args[1]
        elif len(args) == 3:
            return args[0] + args[1] + args[2]
        else:
            raise ValueError("Unsupported number of arguments")

calc = Calculator()

result1 = calc.add(2, 3)
print(result1)  # Outputs: 5

result2 = calc.add(2, 3, 4)
print(result2)  # Outputs: 9
