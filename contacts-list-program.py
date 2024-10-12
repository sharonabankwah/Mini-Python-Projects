# Write a Python program that allows the user to create and manage a contact list.

# Allow the user to add a contact by entering a name and a phone number.
# Ensure the phone number only accepts numeric values.
# Allow the user to view all contacts stored.
# Allow the user to search for a contact by name.
# Allow the user to exit the program.
# Requirements:
# Use a loop to keep the program running until the user chooses to exit.
# Handle any potential errors when the user enters invalid data (e.g., non-numeric phone numbers).
# Use a dictionary to store contacts, where the name is the key and the phone number is the value.

contacts = {}

while True:
    user_question = input("Do you want to add an entry to your contacts list? Enter 'yes' or 'no': ").lower()

    if user_question == "yes":
        contact_name = input("Please enter contact name: ") # continue the program

        try:
            contact_number = int(input("Please enter contact number: ")) # ask user for contact number

            if contact_name and contact_number: # if contact name and number correct, add to dictionary
                contacts[contact_name] = contact_number
                print("Contact has been stored successfully.")

        except ValueError:
            print("Oops... that was not a valid response. Please enter numeric values only.")

    elif user_question == "no":
        print("List of all the contacts you have stored:")
        for name, number in contacts.items():
            print(f"{name}:{number}")
        break

user_search = input("Do you want to search for a contact? Enter 'yes' or 'no': ").lower()

if user_search == "yes":
    contact_search = input("Please enter the contact name: ").lower()

    if contact_search in contacts:
        print("1 result found:")
        print(f"{contact_search}: {contacts[contact_search]}")
    else:
        print("No results found.")
elif user_search == "no":
    print("Search cancelled.")



