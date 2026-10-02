# Level 1 - Q17: Remove Duplicates
# Remove duplicate elements from a list while maintaining the original order.

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = []

for n in numbers:
    if n not in result:
        result.append(n)

print("List without duplicates:", result)
