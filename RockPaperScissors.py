#Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input), compare them,
#print out a message of congratulations to the winner,
#and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock


print("Choose: Rock, Scissor or Paper")
a = input("Player 1 plays: ")
b = input("Player 2 plays: ")


while (a == "Rock" and b == "Rock"):
    a  = input("Player 1 plays: ")
    b = input("Player 2 plays: ")

while (a == "Scissors" and b == "Scissors"):
    a  = input("Player 1 plays: ")
    b = input("Player 2 plays: ")

while (a == "Paper" and b == "Paper"):
    a  = input("Player 1 plays: ")
    b = input("Player 2 plays: ")

if a == "Rock" and b == "Scissors":
    print("Player 1 wins!")
elif a == "Rock" and b == "Paper":
    print("Player 2 wins!")
elif a == "Scissors" and b == "Rock":
    print("Player w wins!")
elif a == "Scissors" and b == "Paper":
    print("Player 1 wins!")
elif a == "Paper" and b == "Rock":
    print("Player 1 wins!")
elif a == "Paper" and b == "Scissors":
    print("Player 2 wins!")
       



