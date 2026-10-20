def guessingGame():
    attempts = 3
    correctNumber = 7
    guess = input(" guess a number: "))
    while guess != correctNumber:
    
        print("sorry thats incorrect")
        print("try again")
        attempts-=1
        print(attempts)
        guess = int(input())
    if attempts == 0:
        print("you have no more attempts left")