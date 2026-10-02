# Level 3 - Q8: Numbers Until Stop
# Read numbers until stop is entered, handle invalid inputs using try-except, then calculate minimum, maximum, average, and median.

numbers = []

while True:
    value = input("Enter a number (or 'stop' to finish): ")
    if value.lower() == "stop":
        break
    try:
        numbers.append(float(value))
    except ValueError:
        print("Invalid input, please enter a number or 'stop'.")

if not numbers:
    print("No numbers were entered.")
else:
    numbers_sorted = sorted(numbers)
    n = len(numbers_sorted)
    if n % 2 == 0:
        median = (numbers_sorted[n // 2 - 1] + numbers_sorted[n // 2]) / 2
    else:
        median = numbers_sorted[n // 2]

    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
    print("Average:", sum(numbers) / len(numbers))
    print("Median:", median)
