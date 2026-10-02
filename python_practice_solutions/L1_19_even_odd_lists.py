# Level 1 - Q19: Even & Odd Lists
# Separate even and odd numbers from a list into two different lists.

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

evens = [n for n in numbers if n % 2 == 0]
odds = [n for n in numbers if n % 2 != 0]

print("Even numbers:", evens)
print("Odd numbers:", odds)
