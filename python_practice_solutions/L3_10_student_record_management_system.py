# Level 3 - Q10: Student Record Management System
# Create a Student Record Management System using functions, lists, loops, list comprehensions, exception handling, and file handling.

import csv

FILENAME = "students.csv"


def load_students():
    students = []
    try:
        with open(FILENAME, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["marks"] = int(row["marks"])
                students.append(row)
    except FileNotFoundError:
        pass  # no file yet - start with an empty list
    return students


def save_students(students):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["roll_no", "name", "marks"])
        writer.writeheader()
        writer.writerows(students)


def add_student(students):
    roll_no = input("Roll number: ")
    name = input("Name: ")
    try:
        marks = int(input("Marks: "))
    except ValueError:
        print("Invalid marks. Student not added.")
        return
    students.append({"roll_no": roll_no, "name": name, "marks": marks})
    print("Student added.")


def display_students(students):
    if not students:
        print("No records found.")
        return
    for s in students:
        print(s["roll_no"], "-", s["name"], "-", s["marks"])


def search_student(students):
    roll_no = input("Enter roll number to search: ")
    # list comprehension to find all matching students
    matches = [s for s in students if s["roll_no"] == roll_no]
    if matches:
        for s in matches:
            print(s["roll_no"], "-", s["name"], "-", s["marks"])
    else:
        print("Student not found.")


def average_marks(students):
    if not students:
        print("No records found.")
        return
    avg = sum(s["marks"] for s in students) / len(students)
    print("Average marks:", avg)


def main():
    students = load_students()
    while True:
        print("\n1. Add student\n2. Display all\n3. Search\n4. Average marks\n5. Save & Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            average_marks(students)
        elif choice == "5":
            save_students(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
