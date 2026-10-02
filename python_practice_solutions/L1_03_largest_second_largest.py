# Level 1 - Q3: Largest & Second Largest
# Write a program to find the largest and second largest among three numbers.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

largest = max(a, b, c)
second_largest = sorted([a, b, c])[1]

print("Largest:", largest)
print("Second largest:", second_largest)
