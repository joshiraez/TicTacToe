#Made by Jose Raez
#Note that it won't use any OOP because it was just a simple coding practice. Other projects will use it.

def printBoard(currentBoard):
    boardTiles = ('  1 2 3', ' ┌-┬-┬-┐', ' ├-┼-┼-┤', ' └-┴-┴-┘')

    print(boardTiles[0])
    for row in range(2):
        printRow(currentBoard, row)
        print(boardTiles[1])
    printRow(currentBoard, 2)
    print(boardTiles[2])

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
    while result: #None will evaluate to False. String will evaluate to True.
        putPiece(board, player)
        printBoard(board)
        result = checkResult(board)
        player= 2-(player+1)%2
    else:
        #no exception, print result
        print(result)


def putPiece(board, player): #Needs exception handling
    ok = True
    while not ok:
        print('Player {} please introduce row and column for your move').format(player)

        row =  int(input('Row (1-3):'))-1
        while not 0<=row<=2:
            row = int(input('Wrong number. Row (1-3):')) -1

        column = int(input('Column (1-3):'))-1
        while not 0<=column<=2:
            column = int(input('Wrong number. Column (1-3):')) -1

        if board[row][column]==0:
            board[row][column]==player

        else:
            print("You can't put a piece there. Select another position.")
            ok = False

