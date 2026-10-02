# Level 2 - Q20: Menu-Driven Calculator
# Build a menu-driven calculator that handles invalid inputs and division by zero using try-except.

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice.")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered.")
        continue

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        try:
            print("Result:", a / b)
        except ZeroDivisionError:
            print("Error: cannot divide by zero")
