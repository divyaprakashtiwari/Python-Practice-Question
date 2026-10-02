# Level 2 - Q16: Safe Division
# Write a program to safely divide two numbers using exception handling.

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:
    print("Error: please enter valid numbers")
