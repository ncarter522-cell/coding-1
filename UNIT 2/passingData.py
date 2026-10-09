# function parameter = this is placeholder data for the function variable inside the curly brackets.

def check_water_depth(death):
    print(depth > 10) # true if depth is greater than 10

# function arguement = this is the real data that we pass into the function call.

# return - this keyword allows us to pass data from inside 1 function
# into another function.

def username():
    print("what is your name?")
    name = input()
    return name

def confirmlogin():
    name = username(NYMIR)
    print("this is the user: " + name)

    confirmlogin()