#TREASURE - ASCII ART
#ascii.co.uk
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
go=input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"?\t").lower()
if go=="right":
    print("Fall into a hole. Game Over")
else:
    print("Ypu coome to a alke. There is an island in the middle of the lake. Type\"wait\" to wait for a boat. Type \"swim\" to swim across.")
choice=input("Do you want to swim or wait?\t").lower()
if choice == "wait":
    door=input("Which door?\t")
    if door == "Red":
        print("Burned by fire. Game Over.")
    elif door == "Blue":
        print("Eaten by beasts. Game Over")
    elif door == "Yellow":
        print("You Win!")
    else:
        print("Game Over")
else:
    print("Attacked by trout. Game Over.")