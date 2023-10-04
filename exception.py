try:
 num1 = int(input("Enter a number:"))
 num2 = int(input("Enter another number:"))
 result = num1/num2
 print(f"Result is:{result}")
except ZeroDivisionError:
    print("Error: Division by Zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please input valid number.")
# except Exception as e:
#     print(f"An error occurred: {e}")
else:
    print("No exception were raised.")
finally:
    print("This is the way handle the exceptions in Python.")