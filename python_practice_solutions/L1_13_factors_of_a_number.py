# Level 1 - Q13: Factors of a Number
# Find all factors of a given number.

num = int(input("Enter a number: "))
factors = []

for i in range(1, num + 1):
    if num % i == 0:
        factors.append(i)

print("Factors of", num, ":", factors)
