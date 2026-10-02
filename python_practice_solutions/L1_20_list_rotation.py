# Level 1 - Q20: List Rotation
# Rotate a list by K positions to the left.

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
k = int(input("Enter number of positions to rotate left: "))

k = k % len(numbers)
rotated = numbers[k:] + numbers[:k]

print("Rotated list:", rotated)
