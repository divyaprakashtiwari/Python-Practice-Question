# Level 2 - Q10: Merge & Remove Duplicates
# Write a function that merges two lists and removes duplicate elements.

def merge_unique(list1, list2):
    merged = list1 + list2
    result = []
    for item in merged:
        if item not in result:
            result.append(item)
    return result

print(merge_unique([1, 2, 3], [2, 3, 4, 5]))
