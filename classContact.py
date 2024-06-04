class Contact:

    def __init__(self, name, contactNumber, email):
        self.name = name
        self.contactNumber = contactNumber
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.contactNumber}, Email: {self.email}"
    


    
    

class ContactManagementSystem:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open("phonebook.txt", 'r') as phonebook:
                for line in phonebook:
                    name, contactNumber, email = line.strip().split(',')
                    self.contacts.append(Contact(name, contactNumber, email))
        except FileNotFoundError:
            # If the file does not exist, we assume no contacts have been saved yet
            pass

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

        with open("phonebook.txt", 'a') as phonebook:
            phonebook.write(f"{contact.name},{contact.contactNumber},{contact.email}\n")
        
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            print("Contacts:")
            for idx, contact in enumerate(self.contacts):
                print(f"{idx + 1}. {contact}")

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if not found_contacts:
            print(f"No contact found with the name '{name}'.")
        else:
            print("Search Results:")
            for contact in found_contacts:
                print(contact)

    def delete_contact(self, position):
        if position < 1 or position > len(self.contacts):
            print("Invalid position.")
        else:
            removed_contact = self.contacts.pop(position - 1)
            print(f"Contact '{removed_contact.name}' deleted.")