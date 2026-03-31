class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"\n✅ Contact '{name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\n📂 Your contact book is currently empty.")
            return
        
        print("\n--- Contact List ---")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. {contact.name} - {contact.phone}")
        print("--------------------")

    def search_contact(self, search_term):
        found_contacts = [c for c in self.contacts if search_term.lower() in c.name.lower() or search_term in c.phone]
        
        if not found_contacts:
            print(f"\n❌ No contacts found matching '{search_term}'.")
            return None
        
        print("\n--- Search Results ---")
        for contact in found_contacts:
            print(f"Name:    {contact.name}")
            print(f"Phone:   {contact.phone}")
            print(f"Email:   {contact.email}")
            print(f"Address: {contact.address}")
            print("-" * 20)
        return found_contacts

    def update_contact(self, search_term):
        print("\n🔍 Searching for contact to update...")
        found_contacts = self.search_contact(search_term)
        
        if found_contacts:
            contact = found_contacts[0] 
            print("\nEnter new details (leave blank and press Enter to keep current value):")
            
            new_name = input(f"Name [{contact.name}]: ").strip() or contact.name
            new_phone = input(f"Phone [{contact.phone}]: ").strip() or contact.phone
            new_email = input(f"Email [{contact.email}]: ").strip() or contact.email
            new_address = input(f"Address [{contact.address}]: ").strip() or contact.address
            
            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email
            contact.address = new_address
            print(f"\n✅ Contact '{contact.name}' updated successfully!")

    def delete_contact(self, search_
