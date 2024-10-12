# a program that checks the strength of a user's password

# ask the user for their password input
password = input("Please enter your password here: ")

special_char = "!@£$%^&*()-+_={}[]'<>,.?/"

# a flag to check whether the password has 8 or more characters
has_8_char = False
# a flag to check whether the password has an uppercase letter
has_upper = False
# a flag to check whether the password has a lowercase letter
has_lower = False
# a flag to check whether the password has a digit
has_digit = False
# a flag to check whether the password has a special character
has_special = False
# a counter to count how many conditions are met
num_of_flags_true = 0

# if the length of the password is 8 or greater, set flag to true
if len(password) >= 8:
    has_8_char = True
    num_of_flags_true += 1

# for every character in password
for char in password:
    if not has_upper and char.isupper(): # this means has_upper == false and it checks if there is an upper
        has_upper = True # change it to true once there is an upper found
        num_of_flags_true += 1 # then add it to the counter
    elif not has_lower and char.islower():
        has_lower = True
        num_of_flags_true += 1
    elif not has_digit and char.isdigit():
        has_digit = True
        num_of_flags_true += 1
    elif not has_special and char in special_char:
        has_special = True
        num_of_flags_true += 1

# determine password strength based on the number of true conditions
if num_of_flags_true == 5:
    print("Your password is: STRONG")
elif num_of_flags_true == 3 or num_of_flags_true == 4:
    print("Your password is: MEDIUM")
else:
    print("Your password is: WEAK")

