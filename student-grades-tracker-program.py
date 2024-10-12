# Create a program that allows the user to input student names and their corresponding grades, then store this information in a dictionary. Finally, the program should display the student with the highest grade, the student with the lowest grade, and the average grade of all students.

name_and_grade_dict = {}

while True:
    # Loop to ensure the user inputs 'continue' or 'exit'
    decision_input = input("Welcome! Do you want to store the grades of all the students in your class? Please enter 'continue' or 'exit': ").lower()

    if decision_input == "continue":
        # Now proceed with the rest of the program
        student_input = input("Please enter student name: ").title()

        try:
            # Ask for student grade
            grade_input = int(input("Please enter grade: "))

            # If both values are entered correctly, store values in the dictionary
            if student_input and grade_input:
                name_and_grade_dict[student_input] = grade_input
                print(f"Thank you, {student_input}'s name and grade have been stored successfully.")

        except ValueError:
            print("Oops! That was not a valid response. Please enter a numeric value for the grade.")

    elif decision_input == "exit":
        print("\nFinal list of students and grades:")
        for student, grade in name_and_grade_dict.items():
            print(f"{student}: {grade}")

        # If grades exist, calculate highest, lowest, and average
        if name_and_grade_dict:
            grades = list(name_and_grade_dict.values())  # Extract all the grades

            highest_grade = max(grades)  # Get the highest grade
            lowest_grade = min(grades)   # Get the lowest grade
            average_grade = sum(grades) / len(grades)  # Calculate the average grade

            print(f"\nThe highest grade is: {highest_grade}")
            print(f"The lowest grade is: {lowest_grade}")
            print(f"The average grade is: {average_grade:.2f}")  # Display average rounded to 2 decimal places
        else:
            print("No grades have been entered.")
        exit()  # End the program completely

    else:
        print("Invalid input. Please enter 'continue' or 'exit'.")  # Loop again if the input is invalid
