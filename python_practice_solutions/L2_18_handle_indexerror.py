# Level 2 - Q18: Handle IndexError
# Handle IndexError while accessing list elements.

my_list = [10, 20, 30]

try:
    index = int(input("Enter an index: "))
    print("Value:", my_list[index])
except IndexError:
    print("Error: index out of range")
except ValueError:
    print("Error: please enter a valid integer")
