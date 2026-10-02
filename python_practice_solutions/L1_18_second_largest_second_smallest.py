# Level 1 - Q18: Second Largest & Second Smallest
# Find the second largest and second smallest element in a list.

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
unique_sorted = sorted(set(numbers))

print("Second smallest:", unique_sorted[1])
print("Second largest:", unique_sorted[-2])
