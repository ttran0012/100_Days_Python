# Description
# Create a Tip calculator
# Formula  ( bill_amount * tip percentage) * people

# Welcome to the TIP Calculator! (message)
# Ask for the Total Bill!
    # get_input = input("Get Total Bill")
# How much tip to give 10, 15, 20, 25 %
    # get_tip_input = input("")
    # if user input = 10 or 15  or 20 or 25
    # then calculate
    # else invalid number

print("Welcome to the TIP CALCULATOR!")
get_bill = float(input("What was the total Bill? "))
get_tip_input = int(input("How much tip would you like to tip? 10 %, 15%, 20% or 25%"))
get_split = int(input("How many people to split the bill? "))

# Define Function for calculation
def tip_calculation(bill, tip_percentage, people):
    tip_percentage = tip_percentage / 100
    total_tip = bill * tip_percentage
    total_bill = bill + total_tip
    each_person_pay = total_bill / people
    return each_person_pay

print(f"Each Person would Pay: {tip_calculation(get_bill,get_tip_input, get_split):.2f}")

