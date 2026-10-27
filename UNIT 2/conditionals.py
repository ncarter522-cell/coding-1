def movieTicket():
    print("welcome to the theater. How old are you: ")
    userage = int(input())
    if userage <= 7:
        print("your ticket is 8.00")
    else:
        print("sorry, there was an error")

def movieTicket2():
    print("welcome to the theater. what is your age: ")
    userage = int(input())
    if userage >= 8 and userage <= 12:
        print("your ticket is 20.00")
    else:
        print("sorry, there was an error")
