def guessingGame():
    attempts = 3
    correctNumber = 7
    guess = input(" guess a number: ")
    while guess != correctNumber:
    
        print("sorry thats incorrect")
        print("try again")
        attempts-=1
        print(attempts)
        guess = int(input())
    if attempts == 0:
        print("you have no more attempts left")


def passwordReset():
    passwordTries = 5
    PasswordCorrect = 1991
    enter = input(" In order to reset your password type in your old password: ")

    if attempts> 0:
    while enter != PasswordCorrect: 1991

    print("sorry thats incorrect")
    print("try again")
    passwordTries-=1
    print(passwordTries)
    enter = int(input())
if attempts == 0:
    print("you have no more attempts. please try again later: " + str(attempts))
    print("you cannot get no more retries")

    print("you are successfully login")



passwordReset