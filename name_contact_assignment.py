import re

contacts = []

def validate_phone(phone):
    if not re.match(r'^[\d\-]+$', phone):
        print("Invalid phone! Use only digits and hyphens.")
        return False
    return True

def validate_email(email):
    if email and ("@" not in email or "." not in email):
        print("Invalid email! Must contain @ and .")
        return False
    return True

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    if not validate_phone(phone):
        return
    email = input("Email: ").strip()
    if not validate_email(email):
        return
    contacts.append((name, phone, email))
    print("Contact added!")

def view_contact():
    name = input("Enter name: ").strip()
    for c in contacts:
        if c[0].lower() == name.lower():
            print(f"Name: {c[0]}, Phone: {c[1]}, Email: {c[2]}")
            return
    print("Not found.")

def update_contact():
    name = input("Enter name to update: ").strip()
    for i, c in enumerate(contacts):
        if c[0].lower() == name.lower():
            phone = input(f"Phone ({c[1]}): ") or c[1]
            if phone != c[1] and not validate_phone(phone):
                return
            email = input(f"Email ({c[2]}): ") or c[2]
            if email != c[2] and not validate_email(email):
                return
            contacts[i] = (c[0], phone, email)
            print("Updated!")
            return
    print("Not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    for i, c in enumerate(contacts):
        if c[0].lower() == name.lower():
            contacts.pop(i)
            print("Deleted!")
            return
    print("Not found.")

def search_contacts():
    query = input("Search (name/phone/email): ").strip().lower()
    results = [c for c in contacts if query in c[0].lower() or query in c[1] or query in c[2].lower()]
    if not results:
        print("No matches.")
        return
    print(f"{'Name':<20} {'Phone':<15} {'Email':<25}")
    print("-" * 60)
    for c in results:
        print(f"{c[0]:<20} {c[1]:<15} {c[2]:<25}")

def list_all():
    if not contacts:
        print("No contacts.")
        return
    print(f"{'Name':<20} {'Phone':<15} {'Email':<25}")
    print("-" * 60)
    for c in contacts:
        print(f"{c[0]:<20} {c[1]:<15} {c[2]:<25}")

def main():
    while True:
        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")
        ch = input("Choose (1-7): ")
        if ch == "1": add_contact()
        elif ch == "2": view_contact()
        elif ch == "3": update_contact()
        elif ch == "4": delete_contact()
        elif ch == "5": search_contacts()
        elif ch == "6": list_all()
        elif ch == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
