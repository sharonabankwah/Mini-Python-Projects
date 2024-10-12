# create an age calculator that calculates how long a user has left until they turn 100 years old

# greet the user
greeting = "Welcome!"
print(greeting)

# ask the user for their name
name = input("What's your name? ")

# see if the user puts a valid input
while True:
     try:
         age = int(input("What's you are age? "))
         if age <= 0:
             print("Please enter a valid age... ")
         else:
             break
     except ValueError:
         print("Oops! That was not a valid number, try again... ")

# store the calculation of 100 subtract user's age to a variable
years_until_100 = 100 - age

# confirm and display result
print(f"Thank you {name}, to confirm you are {age} years old.")
print(f"You have {years_until_100} years until you turn 100!")


