from LedHandler import LedHandler

class Board:
    def __init__(self):
        self.board = self.createBoard()

    def createBoard(self, ROWS=11, COLUMNS=14):
        board = []
        for rows in range(ROWS):
            board.append([])
            for columns in range(COLUMNS):
                board[-1].append(" ")
        return board

    def lightGreen(self, row=0, column=0):
        self.board[row][column] = "green"

    def lightBlue(self, row=0, column=0):
        self.board[row][column] = "blue"

    def lightRed(self, row=0, column=0):
        self.board[row][column] = "red"

    def lightClear(self, row=0, column=0):
        self.board[row][column] = " "

    # DEBUG
    def printBoard(self):
        print(self.board)
