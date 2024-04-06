print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('''
Welcome to Treasure Island.
Your goal is to find the treasure.
''')

choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()

if choice1 == 'left':
    print("You arrive at a lake. There is an island in the middle of the lake. "
          "Type 'wait to wait for a boat. Type 'swim to swim across")
    choice2 = input().lower()

    if choice2 == 'wait':
        print('You arrive at the island unharmed. There is a house with 3 doors. '
              'One yellow, one red, and one blue. Which color do you choose?')
        choice3 = input().lower()

        if choice3 == 'blue':
            print('You enter a room full of beasts. Game over!')

        elif choice3 == 'red':
            print('You enter a room of fire at temperatures exceeding the sun. Game over!')

        elif choice3 == 'yellow':
            print('You found the treasure. You\'re my hero!!!')

        else:
            print('You just carry your hand kill yourself 🙄')

    elif choice2 == 'swim':
        print('There are human eating sharks in the lake. Game over!')

    else:
        print('You just carry your hand kill yourself unnecessarily 🙄')

elif choice1 == 'right':
    print('You fall into a pit filled with snakes. Game over!')

else:
    print('You just carry your hand give yourself unnecessary death 🙄')