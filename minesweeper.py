import random

class Cell:
    def __init__(self):
        self.clicked = False
        self.mine = False
        self.number = False
    
    def show(self):
        if self.mine:
            return 'X'
        else:
            return self.number

class Grid:
    def __init__(self, size=5, number_of_mines = 5):
        self.size = size
        self.buildGrid(size)
        self.seedMines(number_of_mines)
        self.populateNumbers()
        
    def buildGrid(self, size):
        self.grid = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Cell())
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

class Game:
    def __init__(self):
        self.grid = Grid()
    
    def debug(self):
        self.grid.showGrid()

        
g = Game()
g.debug()
        