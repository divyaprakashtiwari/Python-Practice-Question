# Level 1 - Q7: Character Classification
# Count the number of vowels, consonants, digits, and special characters in a string.

s = input("Enter a string: ")
vowels = consonants = digits = special = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif not ch.isspace():
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)
