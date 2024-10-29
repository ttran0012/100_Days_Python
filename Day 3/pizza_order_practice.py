# Write a Pizza Delivery Program
'''
    Based on a user's order, work out their final bill. Use the input() function to get user's
        preferences and then add up the total of their order and tell them how much they have
            to pay

    SIZE:
        small pizza (s): $15
        medium pizza (m): $20
        large pizza (l): $25

    TOPPING:
        peperoni (p) : $2
        cheese (c) : $0

'''

print("Welcome to TAN PIZZERIA!\n")

def ask_size_of_pizza():
    small_pizza = 15
    medium_pizza = 20
    large_pizza = 25
    print("What size of Pizza would you like to order? \n -----(s) (m) (l)-----")

    while True:
        get_pizza_size = input("Small pizza (s): $15\nMedium pizza (m): $20\nLarge pizza (l): $25\n")
        if get_pizza_size == 's' or get_pizza_size == 'S':
            return small_pizza
        elif get_pizza_size == 'm' or get_pizza_size == 'M':
            return medium_pizza
        elif get_pizza_size == 'l' or get_pizza_size == 'L':
            return large_pizza
        else:
            print("Invalid Choice! Please select (s) or (m) or (l)")

def ask_for_topping():
    print("Nice Choice! What would you like for topping?\n")
    peperoni = 2
    sausage = 3
    while True:
        get_topping = input("Peperoni (P) $2 or Sausage (S) $3 ")
        if get_topping == 'p' or get_topping == 'P':
            return peperoni
        elif get_topping == 's' or get_topping == 'S':
            return sausage
        else:
            print("Invalid Choice! Please select (p) or (s)")

def cal_total(x,y):
    return (x+y) * 0.4

while True:
    ask_user = input("Would you like to order a pizza? Y or N?")

    if ask_user == 'Y' or ask_user == 'y':
        print("Let order some pizza")
        pizza = ask_size_of_pizza()
        topping = ask_for_topping()
        print(f"Your total is : ${cal_total(pizza, topping):.2f} With Tax")
        break
    elif ask_user == 'N' or ask_user == 'n':
        print("Have a good day!")
        break
    else:
        print("Sorry I did not understand that! Please try again")

