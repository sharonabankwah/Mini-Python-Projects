# a program that asks the user three simple questions

def questions():
    # set user score to 0
    user_score = 0
    # ask question one to user
    input_one = input("What is the capital of France? A) London B) Berlin C) Paris D) Madrid: ").lower()
    if input_one == "paris":
        print("Correct. Next question...")
        user_score += 1
    else:
        print("Incorrect. Next question...")

    # ask question two to user
    input_two = input("What is the largest planet in our solar system? A) Earth B) Jupiter C) Mars D) Saturn: ").lower()
    if input_two == "jupiter":
        print("Correct. Next question...")
        user_score += 1
    else:
        print("Incorrect. Next question...")

    # ask question three to user
    input_three = input("What is 2 + 2? A) 3 B) 4 C) 5 D) 6: ")
    if input_three == "4":
        print("Correct...")
        user_score += 1
    else:
        print("Incorrect...")

    if user_score == 3:
        print(f"Great job! You scored {user_score}/3 on this quiz.")
    elif user_score == 2:
        print(f"Almost there! You scored {user_score}/3 on this quiz.")
    else:
        print(f"Whoops! You scored {user_score}/3 on this quiz.")

questions()

