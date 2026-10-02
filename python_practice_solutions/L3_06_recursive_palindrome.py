# Level 3 - Q6: Recursive Palindrome
# Write a recursive function to determine whether a string is a palindrome.

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

text = input("Enter a string: ")
print("Palindrome:", is_palindrome(text))
