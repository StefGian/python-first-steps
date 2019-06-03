boardSize = int(input("What size of game board do you prefer? "))

def horizLine():
    print(" ---" * boardSize)

def vertLine():
    print("|   " * (boardSize + 1))


for i in range(boardSize):
    horizLine()
    vertLine()
horizLine()

