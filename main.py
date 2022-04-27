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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction=input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()

if direction == "left":
    wait_or_swim=input("You've come to a lake. There is an island in the middle of the lake. "
                       "Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if wait_or_swim=="wait":
        door=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue."
                   "Which colour do you choose? Type 'red','yellow' or 'blue'\n").lower()
        if door == "red":
            print("Congratulations! You found the treasure.")
        elif door== "blue":
            weapon = input("You entered a room full of beasts. Choose your weapon, sword or bat."
                           "Type 'sword' or 'bat'.\n").lower()
            if weapon == "sword":
                print("Congratulations, you are able to escape. Now run for your life and forget the treasure.")
            else:
                print("A bat isn't enough to defeat beasts. You die. Game Over.")
        else:
            print("You entered a room of fire. Game Over.")
    if wait_or_swim == "swim":
        print("You encounter a group of trouts. Game Over.")



if direction== "right":
    print("You fell into a hole. Game Over.")