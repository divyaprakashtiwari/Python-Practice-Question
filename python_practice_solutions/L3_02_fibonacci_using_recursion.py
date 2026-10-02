# Level 3 - Q2: Fibonacci Using Recursion
# Generate the Fibonacci sequence using recursion.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter number of terms: "))
for i in range(terms):
    print(fibonacci(i), end=" ")
print()
