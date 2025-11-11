import streamlit as st

from src.main import ContactBook

st.title("simple CRUD app")
# keep the ContactBook instance in session_state so data isn't lost on reruns
if "book" not in st.session_state:
    st.session_state.book = ContactBook()
book = st.session_state.book
menu = ["Add Contact", "Update Contact", "View Contacts", "Delete Contact"]
choice = st.sidebar.selectbox("Menu", menu)
if choice == "Add Contact":
    st.subheader("Add New Contact")
    name = st.text_input("Enter name:")
    phone = st.text_input("Enter phone:")
    email = st.text_input("Enter email (optional):")
    if st.button("Add Contact"):
        book.add_contact(name, phone, email)
        st.success(f'Contact {name} added successfully.')
elif choice == "Update Contact":
    st.subheader("Update Contact")
    name = st.text_input("Enter name:")
    phone = st.text_input("Enter new phone (leave blank to keep unchanged):")
    email = st.text_input("Enter new email (leave blank to keep unchanged):")
    if st.button("Update Contact"):
        book.update_contact(name, phone if phone else None, email if email else None)
        st.success(f'Contact {name} updated successfully.')
elif choice == "View Contacts":
    st.subheader("View Contacts")

    # support common attribute names and avoid crashing if structure differs
    contacts = getattr(book, "contact", None) or getattr(book, "contacts", None) or {}

    # ensure we have a dict-like object
    contacts = contacts or {}

    if not contacts:
        st.info("No contacts found.")
    else:
        for name, info in contacts.items():
            st.write(f'Name: {name}')
            # use .get to avoid KeyError and show empty string when missing
            st.write(f'Phone: {info.get("phone", "")}')
            st.write(f'Email: {info.get("email", "")}')
            st.write("-" * 50)
elif choice == "Delete Contact":
    st.subheader("Delete Contact")
    name = st.text_input("Enter name:")
    if st.button("Delete Contact"):
        book.delete_contact(name)
        st.success(f'Contact {name} deleted successfully.')


