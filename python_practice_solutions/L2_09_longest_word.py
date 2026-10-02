# Level 2 - Q9: Longest Word
# Write a function that accepts a sentence and returns the longest word.

def longest_word(sentence):
    words = sentence.split()
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

print(longest_word("Python is an amazing programming language"))
