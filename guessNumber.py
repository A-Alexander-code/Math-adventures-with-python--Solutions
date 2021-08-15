from random import randint

def numberGame():
    # choose a random number
    # between 1 and 100
    number = randint(1,15)
    print("I'm thinking of a number between 1 and 100")
    guess = int(input("What's your guess?\n"))
    retry = False
    while retry == False:
        if number == guess:
            print("That's correct! The number was ", number)
            retry = True
            break
        elif number > guess:
            print("Nope. Higher.")
        else:
            print("Nop. Lower")
        guess = int(input("What's your guess?\n"))

numberGame()