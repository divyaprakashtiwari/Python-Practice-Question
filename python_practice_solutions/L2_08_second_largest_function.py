# Level 2 - Q8: Second Largest Function
# Write a function that returns the second largest element of a list.

def second_largest(nums):
    unique_sorted = sorted(set(nums))
    return unique_sorted[-2]

print(second_largest([10, 20, 4, 45, 99]))
