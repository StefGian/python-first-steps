#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low,
#too high, or exactly right.

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends,
#print this out.


import random


randomNum = random.randint(1,9)
guess = 0
count = 0

while guess != randomNum and guess != "exit":
    guess = input("Take a guess: ")
    if guess == "exit":
        break
    guess = int(guess)
    count = count + 1

    if guess < randomNum:
        print("You guessed too low!")
    elif guess > randomNum:
        print("You guessed too high!")
    else:
        print("Exactly right!!")
        print("It took you ", count, "tries.")
        
    


