import random
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

try_again = 'y'
while try_again == 'y':
    get_input = input("You are at a crossroad where would you like to go?\n Type Left or Right\n")
    if get_input.lower() in ["left" or "right"]:
        outcome = random.choice(["Game Over", "Continue"])
        if outcome == "Game Over":
            print("Oh no! You've encountered danger, Game Over.")
            break
        else:
            print("You have made it safely")
            break
    else:
        print("You've entered an Invalid choice!")

    try_again = input("Would you like to try again? y/n ")
    if try_again == 'n' or try_again == 'N':
        exit()

