import random

class Cell:
    def __init__(self, id):
        self.id = id
        self.clicked = False
        self.mine = False
        self.number = False
    
    def show(self):
        if self.clicked:
            if self.mine:
                return 'X'
            else:
                return self.number
        else:
            return '?'
        
    def click(self):
        print(f'{self.id} clicked.')
        self.clicked = True
        if self.mine == True:
            return 1
        return 0

class Grid:
    def __init__(self, size=6, number_of_mines = 5):
        self.size = size
        self.buildGrid(size)
        self.seedMines(number_of_mines)
        self.populateNumbers()
        
    def buildGrid(self, size):
        self.grid = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Cell(id = str(i)+str(j)))
            self.grid.append(row)
    
    def seedMines(self, number_of_mines):
        mines = 0
        while mines < number_of_mines:
            currentCell = random.choice(random.choice(self.grid))
            if not currentCell.mine:
                mines += 1
                currentCell.mine = True

    def populateNumbers(self):
        for i in range(self.size):
            for j in range(self.size):
                self.grid[i][j].number = self.countAdjacentMines(i,j)
                
    def countAdjacentMines(self, i, j):
        count = 0
        if i > 0:
            count += self.countAdjacentMinesInRow(i-1,j)
        if i < self.size-1:
            count += self.countAdjacentMinesInRow(i+1,j)
        count += self.countAdjacentMinesInRow(i,j)
        return count

    def countAdjacentMinesInRow(self, i, j):
        count = 0
        if self.grid[i][j].mine:
            count += 1
        if j > 0:
            if self.grid[i][j-1].mine:
                count += 1
        if j < self.size-1:
            if self.grid[i][j+1].mine:
                count += 1
        return count
    
    def showGrid(self):
        for row in self.grid:
            print()
            for cell in row:
                print(cell.show(), end='  ')
        print()

class MinesweeperGame:
    def __init__(self):
        self.grid = Grid()
        self.gameOver = False

    def click(self, id):
        i = int(id[0])
        j = int(id[1])
        if self.grid.grid[i][j].click():
            self.endGame()
        if self.grid.grid[i][j].number == 0:
            self.clickAdjacentZeros(i, j)

    def clickAdjacentZeros(self, a, b):
        rows = [a]
        if a > 0:
            rows.append (a-1)
        if a < self.grid.size-1:
            rows.append (a+1)
        cols = [b]
        if b > 0:
            cols.append (b-1)
        if b < self.grid.size-1:
            cols.append (b+1)
        for row in rows:
            for col in cols:
                if self.grid.grid[row][col].clicked == False and self.grid.grid[row][col].number == 0:
                    self.grid.grid[row][col].click()
                    self.clickAdjacentZeros(row, col)
                else:
                    self.grid.grid[row][col].click()
                
    def endGame(self):
        self.gameOver = True
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                self.grid.grid[i][j].clicked = True

    def newGame(self):
        self.__init__()
    
    def debug(self):
        self.grid.showGrid()

g = MinesweeperGame()
g.debug()
