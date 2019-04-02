#A tic-tac-toe program..

theBoard={1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

def displayBoard():
    print(theBoard[1], '|', theBoard[2], '|', theBoard[3])
    print(theBoard[4], '|', theBoard[5], '|', theBoard[6])
    print(theBoard[7], '|', theBoard[8], '|', theBoard[9])

def play(move,symbol):
    if(theBoard[move]==''):
        theBoard[move]=symbol
        game(symbol)

    else:
        print("Wrong move!!")
def playerCount(symbol):
    if symbol=="O":
        symbol="X"
        displayBoard()
        move=int(input("Enter block no. for X:"))
        play(move, symbol)
    else:
        symbol="O"
        displayBoard()
        move=int(input("Enter block no. for O:"))
        play(move, symbol)
def game(symbol):

    for i in [1,2,3]:
        if
            print("U win!!", symbol)
        displayBoard()
    else:
        playerCount(symbol)
playerCount("X")

