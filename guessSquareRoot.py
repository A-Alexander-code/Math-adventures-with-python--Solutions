def average(a,b):
    return (a+b)/2

def squareRoot(num, low, high):
    """Finds the square root of num by
    playing the Number Guessing Game
    strategy by guessing over the 
    renge from "low" to "high" """
    for i in range(20):
        guess = average(low,high)
        if guess**2 == num:
            print(guess)
        elif guess**2 > num:            # Guess lower
            high = guess
        else:                           # Guess higher
            low = guess
        print(str(guess))

squareRoot(50000,220,225)