# Level 1 - Q8: Palindrome Using Slicing
# Check whether a string is a palindrome using slicing.

s = input("Enter a string: ")

if s == s[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
