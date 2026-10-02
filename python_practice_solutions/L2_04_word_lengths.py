# Level 2 - Q4: Word Lengths
# Create a list containing the lengths of each word in a sentence.

sentence = input("Enter a sentence: ")
lengths = [len(word) for word in sentence.split()]
print("Word lengths:", lengths)
