from classContact import Contact
from classContact import ContactManagementSystem 


def main():
    cms = ContactManagementSystem()
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            cms.add_contact(name, phone, email)
        elif choice == '2':
            cms.view_contacts()
        elif choice == '3':
            name = input("Enter the name to search: ")
            cms.search_contact(name)
        elif choice == '4':
            position = int(input("Enter the contact number to delete: "))
            cms.delete_contact(position)
        elif choice == '5':
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        break

if __name__ == "__main__":
    main()

