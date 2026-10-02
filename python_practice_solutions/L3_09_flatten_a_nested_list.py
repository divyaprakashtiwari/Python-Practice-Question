# Level 3 - Q9: Flatten a Nested List
# Write a recursive function to flatten a nested list.

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [1, [2, 3, [4, 5]], 6, [7, [8, [9, 10]]]]
print(flatten(nested))
