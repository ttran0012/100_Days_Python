import random

from IPython.core.inputsplitter import get_input_encoding

print('''   ,     ,_
           |`\    `;;,            ,;;'
           |  `\    \ '.        .'.'
           |    `\   \  '-""""-' /
           `.     `\ /          |`
             `>    /;   _     _ \
              /   / |       .    ;
             <  (`";\ ()   ~~~  (/_
              ';;\  `,     __ _.-'` )
                >;\          `   _.'
                `;;\          \-'
                  ;/           \ _
                  |   ,"".     .` \
                  |      _|   '   /
                   ;    /")     .;-,
              jgs   \    /  __   .-'
                     \,_/-"`  `-'
    
    Welcome to Treasure ISLAND!!!
        Your Mission is to FIND the TREASURE!
''')
def try_again():
    get_try_again = input("Seems like you make a mistake. Would you like to try again? y/n?")
    if get_try_again.lower() == 'y':
        return cross_road()
    elif get_try_again.lower() == 'n':
        print("You must be a terrible player! Goodbye!")
        exit()
    else:
        print("Invalid Choice choose again!")

def good_bye():
    print("Thanks a lot for playing!\nHope you play again soon!!!")
    return exit()


def cross_road():
    print('''          |      |
          |      |
          |      |
          |      |
          |      |
  ========+======+========
          |      |
          |      |
          |      |
          |      |
          |      |
''')
    get_input = input("You are at a Cross Road. Should you \n1.Turn Left\n2.Turn Right")
    if get_input in ["1","2"]:
        outcome = random.choice(["Game Over","Continue"])
        if outcome == "Game Over":
            print("Oh no! You choose the Wrong Path and Fell into a Deep hole!\nWhere A Dragon ate you for Dinner....")
            return try_again()
        elif outcome == "Continue":
            print("Whew...you chose the correct Path! Ain't too bad right? Let's get moving before it get dark.")
            return True
        else:
            print("Invalid choice!")
    else:
        print("Invalid Choice!\nYou broke the system...\nSystem terminating....")

def a_river():
    print("Congrats! on Making pass the Cross Road!\nAfter a long...endless walk you came across a broken bridge...What are you going to do?\n")
    print("1.Swim (An Aligator might get you) OR 2.Wait (A boat might come or a Bear might eat you for dinner)...\nHurry it's getting Dark!")
    get_input = input("Choice is up to you...\n1.SWIM\n2.WAIT")
    if get_input == '2':
        print("Oh ho! Smart! Luckily the Boat made it in time to pick you up before being a Bear Dinner!\nCutting it close there buddy...")
        return True
    else:
        print("Oh no! You chose the wrong choice! You swam half way and got tired and drown...\nAligator Thanks you for a good meal!")
        get_input = input("Would you like to try again? y/n?")
        if get_input.lower() == 'y':
            return a_river()
        else:
            good_bye()

def a_door():
    print('''The boat picked you up...and dropped you off after a while of traveling..
    \nThere is a house to your right...you decided to head there for the night as it's getting dark....
    \nYou reached to the house and there is a huge door....\n
    \n
              ________
             / ______ \
             || _  _ ||
             ||| || |||
             |||_||_|||
             || _  _o|| (o)
             ||| || |||
             |||_||_|||      ^~^  ,
             ||______||     ('Y') )
            /__________\    /   \/
    ________|__________|__ (\|||/) _________
   hjw     /____________\
   `97     |____________| \n
   \nYou knocked and it and no one answered......
   \nThe door slowly creeks and open...
   \nYou got 2 Choices.\n1.Do you want to Entered the house to shelter OR \n2.Leave
    ''')
    get_input = input("This is creepy...oh well....What would you like to do?")
    if get_input == '1':
        print("You sure are a Brave one!")
        return True
    elif get_input == '2':
        print("Oh no...there was a wild pack of wolfs waiting for you...you sure are unlucky....")
        get_input = input("Would you like to try again? y/n?")
        if get_input.lower() == 'y':
            return a_door()
        else:
            good_bye()

def a_hallway():
    print("So you have decided to walk down the long creepy hallway...")
    get_input = input("You Reached the end of the hall there are 2 doors Left and Right\n1.Open Left Door\n2.Open Right Door\n")
    if get_input == '1':
        print("Jack pot! You won!")
        good_bye()
    if get_input == '2':
        print("IDK what's next lol")
    else:
        print("Invalid Choice")
        a_hallway()

def a_left_door():
    print("You are now facing the Left door...hands are trembling...slowly opening the door...")
    print("There's a dinner table...full of delicious food. You are drooling...\n")
    get_input = input("\n1.Do you want to eat? \n2.Back out of the door\n")
    if get_input == '1':
        print("You ate the food on the Table and feel full with energy!")

    elif get_input == '2':
        print("You leave...hungry...")
        a_three_choice()
    else:
        print("Invalid Choice!")
        return a_left_door()

def a_right_door():
    print("You are now facing the Right door...hands are trembling...slowly opening the door...")
    print("\n")



def a_three_choice():
    print('''There is a long creepy hallway in front of you...a door to your Left and a door to your Right.\n
    What would you like to do? Keep going down the long corridor? or Open the door to your Left or Right?\n
    Make careful choice here....
    
     ''')
    get_input = input("\n1.Hallway\n2.Left Door\n3.Right Door\n")
    # hallway
    if get_input == '1':
        a_hallway()
    # left_door
    if get_input == '2':
        a_left_door()

    # right_door
    if get_input == '3':
        a_right_door()



def main():
    print("Welcome to the game...where you will go nowhere! May the luck be in your favor!")
    if cross_road():
        a_river()
        a_door()
        a_three_choice()
    else:
       good_bye()


#run function
if __name__ == "__main__":
    main()