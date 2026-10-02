# Level 1 - Q16: List Statistics
# Find the largest, smallest, and average value in a list.

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]

print("Largest:", max(numbers))
print("Smallest:", min(numbers))
print("Average:", sum(numbers) / len(numbers))
