class Grid:
    def __init__(self):
        self.grid = self.createGrid()

    def createGrid(self, ROWS=11, COLUMNS=14):
        grid = []
        for rows in range(ROWS):
            grid.append([])
            for columns in range(COLUMNS):
                grid[-1].append(" ")
        return grid

    def lightGreen(self, row=0, column=0):
        self.grid[row][column] = "green"

    def lightBlue(self, row=0, column=0):
        self.grid[row][column] = "blue"

    def lightRed(self, row=0, column=0):
        self.grid[row][column] = "red"

    def lightClear(self, row=0, column=0):
        self.grid[row][column] = " "

    # DEBUGGING FUNCTION
    def printGrid(self):
        print(self.grid)
