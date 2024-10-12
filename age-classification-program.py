# a program that asks the user for their age and classifies them as a child, teenager, adult or senior

while True:
# ask the user for their age
    user_age = input("Please enter your age or type 'quit' to exit: ")

    if user_age.lower() == 'quit':
        break # exit the loop if the user types 'quit'

    try:
        user_age = int(user_age) # Convert input to integer

        if not user_age > 0: # check if age is a positive number
            raise ValueError("Please enter a positive number): ")

    # print statements to classify ages
        if user_age <= 13:
            print("You are classified as a child.")
        elif user_age <= 19:
            print("You are classified as a teenager.")
        elif user_age <= 65:
            print("You are classified as an adult.")
        else:
            print("You are classified as a senior.")

    except ValueError as e:
        print(e) # print the error message for invalid input


