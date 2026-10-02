# Level 2 - Q11: Common Elements
# Find the common elements between two lists without using sets.

def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
