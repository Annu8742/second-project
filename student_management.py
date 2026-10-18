'''Mini Project: Student Management System

Project objective: To develop a Python-based Student Management System that stores student information in a CSV file and allows users to add, search, delete and view student records. All changes are saved permanently in the file.

Features:-
1.Add student records.
2.Search students using their roll number.
3.Delete student records.
4.Display all student records.
5.Store student names, roll numbers and marks in a CSV file.
6.Save changes permanently.'''

import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])


# Read all student records
def read_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


# Add a new student
def add_student():
    roll = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()

    try:
        marks = float(input("Enter marks: "))

        if not roll or not name:
            print("Roll number and name cannot be empty!")
            return

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100!")
            return

        students = read_students()

        for student in students:
            if student["Roll Number"] == roll:
                print("Roll number already exists!")
                return

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([roll, name, marks])

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric marks!")


# Display all students
def display_students():
    students = read_students()

    if not students:
        print("No student records found!")
        return

    print("\n===== STUDENT RECORDS =====")
    print("-" * 45)

    for student in students:
        print("Roll Number:", student["Roll Number"])
        print("Name:", student["Name"])
        print("Marks:", student["Marks"])
        print("-" * 45)


# Search student by roll number
def search_student():
    roll = input("Enter roll number to search: ").strip()
    students = read_students()

    for student in students:
        if student["Roll Number"] == roll:
            print("\nStudent Found!")
            print("Roll Number:", student["Roll Number"])
            print("Name:", student["Name"])
            print("Marks:", student["Marks"])
            return

    print("Student not found!")


# Delete a student
def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    students = read_students()

    updated_students = [
        student for student in students
        if student["Roll Number"] != roll
    ]

    if len(updated_students) == len(students):
        print("Student not found!")
        return

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["Roll Number", "Name", "Marks"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(updated_students)

    print("Student deleted successfully!")


# Main program
def main():
    initialize_file()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice! Please select 1 to 5.")


if __name__ == "__main__":
    main()