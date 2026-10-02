# Level 3 - Q4: Reverse a String Using Recursion
# Reverse a string using recursion.

def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

text = input("Enter a string: ")
print("Reversed:", reverse_string(text))
