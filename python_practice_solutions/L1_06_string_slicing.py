# Level 1 - Q6: String Slicing
# Input a string and print the first 3 characters, last 3 characters, every alternate character, and the reversed string.

s = input("Enter a string: ")

print("First 3 characters:", s[:3])
print("Last 3 characters:", s[-3:])
print("Every alternate character:", s[::2])
print("Reversed string:", s[::-1])
