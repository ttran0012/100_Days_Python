import random

print('''
Rock 
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
\nPaper
 ---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
\nScissors
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  

\nWelcome to ROCK | PAPER | SCISSOR | Game !
\nPress (1) for ROCK
\nPress (2) for PAPER
\nPress (3) for SCISSORS
''')

# Function for user
def user_choice():
    get_choice = input("\nWhat will you choose?\n")
    if get_choice == '1':
        print("You choose ROCK!")
        return get_choice
    elif get_choice == '2':
        print("You choose PAPER!")
        return get_choice
    elif get_choice == '3':
        print("You choose SCISSORS!")
        return get_choice
    else:
        print("Invalid! Please Try Again!")
        user_choice()

# Function for computer
def comp_choice():
    random_choice = random.randrange(1, 3)
    if random_choice == 1:
        print("Computer chooses ROCK!")
        return random_choice
    elif random_choice == 2:
        print("Computer chooses PAPER!")
        return random_choice
    else:
        print("Computer chooses SCISSORS!")
        return random_choice

# Compare
def compare_both(x,y):
    user_choice1 = x
    comp_choice1 = y
    if user_choice1 == 1 and comp_choice1 == 1:
        return print("You both chooses ROCK!")
    elif user_choice1 == 2 and comp_choice1 == 2:
        return print("You both chooses PAPER!")
    elif user_choice1 == 3 and comp_choice1 == 3:
        return print("You both chooses SCISSORS!")
    elif user_choice1 == 1 and comp_choice1 == 2:
        return print("You chooses ROCK and Comp chooses PAPER\nPAPER Beats Rock - Comp Win!")
    elif user_choice1 == 1 and comp_choice1 == 3:
        return print("You chooses ROCK and Comp chooses SCISSORS\nROCK Beats SCISSORS - You Win!")
    elif user_choice1 == 2 and comp_choice1 == 1:
        return print("You chooses PAPER and Comp chooses ROCK\nPAPER Beats ROCK - You Win!")
    elif user_choice1 == 2 and comp_choice1 == 3:
        return print("You chooses PAPER and Comp chooses SCISSORS\nROCK Beats SCISSORS - Comp Win!")
    elif user_choice1 == 3 and comp_choice1 == 1:
        return print("You chooses SCISSORS and Comp chooses ROCK\nROCK Beats SCISSORS - Comp Win!")
    elif user_choice1 == 3 and comp_choice1 == 2:
        return print("You chooses SCISSORS and Comp chooses PAPER\nSCISSORS CUTS PAPER - You Win!")
    else:
        return



# Main
def main():
    x = user_choice()
    y = comp_choice()
    compare_both(x,y)
# To run Function
if __name__ == "__main__":
        main()