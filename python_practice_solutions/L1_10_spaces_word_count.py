# Level 1 - Q10: Spaces & Word Count
# Remove all spaces from a string and count the number of words.

s = input("Enter a string: ")

no_spaces = s.replace(" ", "")
word_count = len(s.split())

print("String without spaces:", no_spaces)
print("Number of words:", word_count)
