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
        get_pizza_size = input("1.Small pizza (s): $15\n2.Medium pizza (m): $20\n3.Large pizza (l): $25\n")
        if get_pizza_size == '1':
            return small_pizza
        elif get_pizza_size == '2':
            return medium_pizza
        elif get_pizza_size == '3':
            return large_pizza
        else:
            print("Invalid Choice! Please select (1) or (2) or (3)")

def ask_for_topping():
    print("Nice Choice! What would you like for topping?\n")
    peperoni = 2
    sausage = 3
    while True:
        get_topping = input("1.Peperoni (P) $2\n2.Sausage (S) $3 ")
        if get_topping == '1':
            return peperoni
        elif get_topping == '2':
            return sausage
        else:
            print("Invalid Choice! Please select (1) or (2)")

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

