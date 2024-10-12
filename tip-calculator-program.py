# Write a program that asks the user for the total amount of their restaurant bill and the percentage tip
# they would like to leave. The program should then calculate and display the tip amount and the final total (bill + tip)

# ask the user for the restaurant bill amount
restaurant_bill = float(input("Please enter the amount of your restaurant bill: "))

# ask the user how much they would like to tip
restaurant_tip = float(input("Please enter the amount you wish to tip: "))

# calculate the total amount for the user to pay
total_to_pay = restaurant_bill + (restaurant_bill * restaurant_tip / 100)

# calculate the tip the user wants to pay
calculated_tip = restaurant_bill * restaurant_tip / 100

# display the total amount for the user to pay (:.2f ensures values are rounded to two decimal places)
print(f"Your restaurant bill is £{restaurant_bill:.2f} and you wish to pay a tip of {restaurant_tip:.2f}%:")
print(f"That means a tip of £{calculated_tip:.2f}, so your total to pay today is £{total_to_pay:.2f}!")