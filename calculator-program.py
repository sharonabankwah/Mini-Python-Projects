# Create a calculator program, that takes in an input from the user and outputs the results of the calculation required

# function to add two numbers
def add(num1, num2):
    return num1 + num2

# function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

operation = """Select operation:
1. Add
2. Subtract
3. Divide
4. Multiply"""

print(operation)

while True:
    # take input from the user
    choice = input("Enter choice 1, 2, 3 or 4: ")

    # check if their choice is valid
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if choice == "1":
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == "2":
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == "3":
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == "4":
            print(num1, "*", num2, "=", multiply(num1, num2))

        # check if the user wants to do another calculation
        # break the while loop if the answer is no
        next_calculation = input("Do you want to do another calculation? Yes or no: ")
        if next_calculation == "no":
            break
        else:
            print("Invalid input.")