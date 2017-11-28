#Made by Jose Raez
#Note that it won't use any OOP because it was just a simple coding practice. Other projects will use it.

board = [[0,0,0],[0,0,0],[0,0,0]]

def printBoard(currentBoard):
    boardTiles = ['┌-┬-┬-┐', '├-┼-┼-┤', '└-┴-┴-┘']

    print(boardTiles[0])
    for row in range(2):
        printRow(currentBoard, row)
        print(boardTiles[1])
    printRow(currentBoard, 2)
    print(boardTiles[2])

def printRow(currentBoard, row):
    boardRows = [' ', 'O', 'X', '│']
    rowPrint = boardRows[3]
    for column in range(3):
        rowPrint += boardRows[currentBoard[row][column]]
        rowPrint += boardRows[3]
    print(rowPrint)

printBoard(board)