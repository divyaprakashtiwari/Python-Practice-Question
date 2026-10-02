# Level 1 - Q1: Marks, Percentage & Grade
# Write a program to input marks in five subjects and calculate the total, percentage, and grade.

marks = []
for i in range(1, 6):
    m = int(input(f"Enter marks for subject {i}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
