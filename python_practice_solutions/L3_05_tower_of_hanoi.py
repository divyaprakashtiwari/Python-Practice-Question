# Level 3 - Q5: Tower of Hanoi
# Solve the Tower of Hanoi problem using recursion.

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print("Move disk", n, "from", source, "to", target)
    tower_of_hanoi(n - 1, auxiliary, source, target)

disks = int(input("Enter number of disks: "))
tower_of_hanoi(disks, "A", "B", "C")
