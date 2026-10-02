# Level 2 - Q17: Valid Integer Input
# Accept integer input until a valid integer is entered using try-except.

while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")

print("You entered:", num)
