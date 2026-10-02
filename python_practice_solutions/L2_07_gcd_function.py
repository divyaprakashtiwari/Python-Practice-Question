# Level 2 - Q7: GCD Function
# Write a function to calculate the GCD of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD:", gcd(x, y))
