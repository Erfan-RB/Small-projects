#Roll The Dice
import random

def again():
    dices = 0
    while dices == 0:
        chosen_dices = int(input("How many dices do you want to roll: ")).lower()
        break
    while not chosen_dices == dices:
        rolls = random.randit(1,6)
        print(rolls)
        dices +=1

    while True:
        try_again = input("would you like to throw again?(Yes/No)").lower()
        if try_again == "Yes":
            again()
        else:
            return

again()            
