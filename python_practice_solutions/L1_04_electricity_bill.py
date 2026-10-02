# Level 1 - Q4: Electricity Bill
# Write a program to calculate an electricity bill based on slab rates.

units = float(input("Enter units consumed: "))

# Slab rates: first 100 units at 3.5, next 200 at 4.5, rest at 6.0
if units <= 100:
    bill = units * 3.5
elif units <= 300:
    bill = 100 * 3.5 + (units - 100) * 4.5
else:
    bill = 100 * 3.5 + 200 * 4.5 + (units - 300) * 6.0

print("Electricity bill: Rs.", round(bill, 2))
