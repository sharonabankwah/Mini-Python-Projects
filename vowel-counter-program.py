# Write a program that asks the user to input a sentence.
# The program should then count and display how many vowels (a, e, i, o, u) are in the sentence.

# create a list of vowels
vowels = ["a", "e", "i", "o", "u"]

# asks the user for an input, convert to lowercase to handle case sensitivity
vowel_checker = input("Please enter your sentence here: ").lower()

# for loop that iterates over the vowels list and counts if any are in the users input
for letter in vowels:
    if letter in vowel_checker:
        vowels_present = vowel_checker.count(letter) # assigns the count of letters to a variable
        print(letter, "-", vowels_present)