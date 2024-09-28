
def load_contacts(filename): # Loads contact from a file with try and except statement incase file is not found
    contacts = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts.append({'name': name, 'phone': phone, 'email': email})
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(filename, contacts): # Saving Contacts using a while loop
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def add_contact(filename, contacts): # Adding contact taking theur name, phone number , and email
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(filename, contacts)

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("=" * 60)
    print("-" + " " * 22 + "Contact List" + " " * 24 + "-")
    print("=" * 60)
    print("-" + " " * 2 + "Name" + " " * 12 + "Phone" + " " * 14 + "Email" + " " * 16 + "-")
    print("-" * 60)
    sno=1
    for contact in contacts:
        name = contact['name']
        phone = contact['phone']
        email = contact['email']
        print(sno, format(name, "<15"), format(phone, "<15"), format(email, "<15"))
        print("-" * 60)
        sno+=1

    print("=" * 60)

def search_contact(contacts, name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print("Contact not found.")


filename = 'address_book.txt'
contacts = load_contacts(filename)
print("\nAddress Book")
print("1. Add Contact")
print("2. View Contacts")
print("3. Search Contact")
print("4. Exit")
choice = input("Choose an option: ")
while choice != "4":
    if choice == '1':
        add_contact(filename, contacts)
    elif choice == '2':
        view_contacts(contacts)
    elif choice == '3':
        name = input("Enter the name to search: ")
        search_contact(contacts, name)
    else:
        print("Invalid option, please try again.")
    print("\nAddress Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Choose an option: ")

