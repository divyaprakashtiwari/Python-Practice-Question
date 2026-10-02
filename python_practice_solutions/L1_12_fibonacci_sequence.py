# Level 1 - Q12: Fibonacci Sequence
# Generate the Fibonacci sequence up to N terms using loops.

n = int(input("Enter number of terms: "))

a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
