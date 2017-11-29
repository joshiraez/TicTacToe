#Made by Jose Raez
#Note that it won't use any OOP because it was just a simple coding practice. Other projects will use it.

def printBoard(currentBoard):
    boardTiles = ('  1 2 3', ' ┌-┬-┬-┐', ' ├-┼-┼-┤', ' └-┴-┴-┘')

    print(boardTiles[0])
    print(boardTiles[1])
    for row in range(2):
        printRow(currentBoard, row)
        print(boardTiles[2])
    printRow(currentBoard, 2)
    print(boardTiles[3])

def printRow(currentBoard, row):
    boardRows = (' ', 'O', 'X', '│')
    rowPrint = str(row +1) + boardRows[3]
    for column in range(3):
        rowPrint += boardRows[currentBoard[row][column]]
        rowPrint += boardRows[3]
    print(rowPrint)

def game():
    board = ([0, 0, 0], [0, 0, 0], [0, 0, 0])
    printBoard(board)
    result = None
    player = 1
    while result is None:
        putPiece(board, player)
        printBoard(board)
        result = checkResult(board)
        player= 2-(player+1)%2
    else:
        #no exception, print result
        print(result)


def putPiece(board, player):
    okPosition = False
    okRow =False
    okColumn=False

    while not okPosition:
        print('Player {} please introduce row and column for your move'.format(player))

        while not okRow:
            try:
                row =  int(input('Row (1-3):'))-1
                if not 0<=row<=2:
                    print('Wrong number.')
                    okRow=False
                else:
                    okRow = True
            except ValueError:
                print('Input a number please')
                okRow=False

        while not okColumn:
            try:
                column = int(input('Column (1-3):'))-1
                if not 0<=column<=2:
                    print('Wrong number.')
                    okColumn=False
                else:
                    okColumn=True
            except ValueError:
                print('Input a number please')
                okColumn = False

        if board[row][column]==0:
            board[row][column]=player
            okPosition = True
        else:
            print("You can't put a piece there. Select another position.")
            okPosition = False

def checkResult(board):
    from collections import Counter
    openPieces=0
    possibleResults = ('Draw', 'Player 1 wins', 'Player 2 wins')
    result=None

    #rows
    # we could use break, but I think it's generally better to avoid sequence breaking
    for row in range(3):
        count = Counter(board[row])
        if count[0] > 0:
            openPieces += count[0]
        elif count[1] == 3:
            result = possibleResults[1]
        elif count[2] == 3:
            result = possibleResults[2]

    if result is None:
        #columns
        for column in range(3):
            count = Counter([row[column] for row in board])
            if count[1] == 3:
                result = possibleResults[1]
            elif count[2] == 3:
                result = possibleResults[2]

        #diagonals:
        count = Counter([board[i][i] for i in range(3)])
        if count[1] == 3:
            result = possibleResults[1]
        elif count[2] == 3:
            result = possibleResults[2]

        count = Counter([board[2-i][i] for i in range(3)])
        if count[1] == 3:
            result = possibleResults[1]
        elif count[2] == 3:
            result = possibleResults[2]

    if result is None and openPieces == 0:
        result = possibleResults[0]

    return result

#mainProgram
game()

