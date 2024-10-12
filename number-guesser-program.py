# Write a program where the computer selects a random number between 1 and 100, and the user has to guess it.
# After each guess, the program should tell the user if their guess is too high, too low, or correct.
# The game should continue until the user guesses the correct number.

# import random module
import random

# computer selects a random number between 1-100
random_num = random.randint(1, 100)

# user inputs a guess
user_guess = int(input("Please enter your guess: "))

# computer checks if user_guess is correct
while True: # while any of the below conditions are true
    if user_guess < random_num:
        print("Your guess was too low...")
        user_guess = int(input("Please try again: ")) # user inputs another guess
    elif user_guess > random_num:
        print("Your guess was too high...")
        user_guess = int(input("Please try again: "))
    else:
        print(f"Game over! You've guessed the correct number: {random_num}")
        break # breaks out of loop when user guesses correctly
