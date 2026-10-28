def vendingMachine():
    print("VENDING MACHINE")
    print("Please type in a value for the item you want: ")
    userSelection = input()
    while userSelection != 'q':
        if userSelection == "b":
            print("nacho chips")

    
    
    print("VENDING MACHINE IS OFF")
vendingMachine()
 
import random
def diceGame():
    print("DICE GAME IS RUNNING")
    print("Please enter r to roll and q to quit: ")
    userselection = input()

    while userselection != 'q':
        if userselection == "r":
            randomnumber = random.randint(1,7)
            if randomnumber == 7
               print(randomnumber)
               print("You win")
               print('-5 points')
               print("Please enter r to roll and q to quit: ")
               userselection = input()

            elif randomnumber == 7:
                print(randomnumber)
                print('YOU WIN!!!')
                print()