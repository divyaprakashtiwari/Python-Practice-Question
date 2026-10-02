# Level 2 - Q13: Element Frequency
# Find the frequency of every element in a list.

def element_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

print(element_frequency([1, 2, 2, 3, 3, 3, 4]))
