import json
import os

CONTACTS_FILE = "contacts.json"



def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)



def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)



def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("Contact added successfully!\n")



def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return

    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} | {contact['phone']} | {contact['email']}")
    print()



def edit_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    index = int(input("Enter the contact number to edit: ")) - 1

    if 0 <= index < len(contacts):
        print("Leave blank to keep old value.")

        name = input(f"New name ({contacts[index]['name']}): ") or contacts[index]['name']
        phone = input(f"New phone ({contacts[index]['phone']}): ") or contacts[index]['phone']
        email = input(f"New email ({contacts[index]['email']}): ") or contacts[index]['email']

        contacts[index] = {"name": name, "phone": phone, "email": email}
        save_contacts(contacts)
        print("Contact updated successfully!\n")
    else:
        print("Invalid contact number.\n")



def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return

    index = int(input("Enter the contact number to delete: ")) - 1

    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        print("Contact deleted successfully!\n")
    else:
        print("Invalid contact number.\n")



def main():
    contacts = load_contacts()

    while True:
        print("====== Contact Management System ======")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")



main()
