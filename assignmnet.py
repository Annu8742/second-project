#1.Contact Book Using Dictionary
#Features: Add, Search, Update aur Delete contacts.

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        if contacts:
            for name, phone in contacts.items():
                print(name, ":", phone)
        else:
            print("Contact book is empty!")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice! Please try again.")


#2.Word Counter from Text File
#Features: Count words, lines and characters in a text file.

try:
    with open("sample.txt", "r") as file:
        text = file.read()

    words = text.split()
    lines = text.splitlines()
    characters = len(text)

    print("===== WORD COUNTER =====")
    print("Total Words:", len(words))
    print("Total Lines:", len(lines))
    print("Total Characters:", characters)

except FileNotFoundError:
    print("Error: sample.txt file not found!")

#3.JSON File Reader
#Features: Read JSON data from a file and print formatted output.

import json

try:
    with open("students.json", "r") as file:
        data = json.load(file)

    print("===== STUDENT DETAILS =====")

    for student in data["students"]:
        print("\nName:", student["name"])
        print("Roll Number:", student["roll_number"])
        print("Marks:", student["marks"])

except FileNotFoundError:
    print("Error: students.json file not found!")

except json.JSONDecodeError:
    print("Error: Invalid JSON format!")