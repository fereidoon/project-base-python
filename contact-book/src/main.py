from collections import defaultdict

class ContactBook:
    def __init__(self) -> None:
        self.contact = defaultdict(dict)
    def add_contact(self,name,phone,email = None):
        if name in self.contact:
            print("Contact already exists.")
            return
                 
        self.contact[name]['phone'] = phone
        self.contact[name]['email'] = email
        print(f'Contact {name} added successfully.')
    def update_contact(self,name,phone= None,email = None):
        if name not in self.contact:
            print("Contact does not exist.")
            return
        if phone:
            self.contact[name]['phone'] = phone
        if email:
            self.contact[name]['email'] = email
        print(f'Contact {name} updated successfully.')

    def view_contact(self,):
        for name ,info  in self.contact.items():
            print(f'name :{name}')
            print(f'phone :{info['phone']}')
            print(f'email : {info['email']}')
            print("-"*50)
    def delete_contact(self,name):
        if name not in self.contact:
            print('Contact does not exitst.')
            return
        del self.contact[name]
        print(f'Contact {name} deleted successfully.')

if __name__ == "__main__":

    book = ContactBook()
    while True:
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. View Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email (optional): ")
            book.add_contact(name,phone,email)
        elif choice == '2':
            name = input("Enter name: ")
            phone = input("Enter new phone (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            book.update_contact(name,phone if phone else None,email if email else None)
        elif choice == '3':
            book.view_contact()
        elif choice == '4':
            name = input("Enter name: ")
            book.delete_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
