# Level 1 - Q15: Floyd's Triangle
# Print Floyd's Triangle up to N rows.

n = int(input("Enter number of rows: "))
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
