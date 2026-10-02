# Level 1 - Q9: Character Frequency
# Find the frequency of each character in a string.

s = input("Enter a string: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch, count in freq.items():
    print(repr(ch), ":", count)
