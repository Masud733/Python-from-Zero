def check_eligibility(result):
    if result >= 40:
        return True
    else:
        return False

try:
    result = float(input("Enter the student's result: "))
    if result < 0 or result > 100:
        print("Invalid result! Please enter a valid result between 0 and 100.")
    else:
        if check_eligibility(result):
            print("The student is eligible for the exam.")
        else:
            print("The student is not eligible for the exam.")
except ValueError:
    print("Invalid input! Please enter a valid numeric result.")










