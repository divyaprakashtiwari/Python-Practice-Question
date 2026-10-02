# Level 2 - Q14: Sort Without sort()
# Sort a list in ascending order without using the sort() method.

def bubble_sort(lst):
    lst = lst[:]  # work on a copy so the original list is untouched
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([5, 2, 9, 1, 5, 6]))
