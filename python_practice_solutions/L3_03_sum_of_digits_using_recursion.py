# Level 3 - Q3: Sum of Digits Using Recursion
# Find the sum of digits of a number using recursion.

def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
