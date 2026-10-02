# Level 2 - Q12: Missing Number
# Find the missing number from a list containing numbers from 1 to N.

def find_missing(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

nums = [1, 2, 4, 5, 6]
print("Missing number:", find_missing(nums, 6))
