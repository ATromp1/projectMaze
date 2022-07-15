import random
import numpy as np


class Tile:
    def __init__(self, col, row, value=''):
        self.row = row
        self.col = col
        self.value = value

    def __repr__(self):
        return self.value


class Grid:
    def __init__(self, width, height, start, value=''):
        self.width = width
        self.height = height
        self.data = np.ndarray(shape=(width, height), dtype=Tile)
        for col in range(height):
            for row in range(width):
                self.data[row][col] = Tile(col, row, value)

        self.current_tile = self.data[start[0]][start[1]]
        self.history = []

    def set(self, col, row, value):
        self.data[col][row].value = value

    def get(self, col, row):
        return self.data[col][row]

    def printGrid(self):
        print(self.data)

    def move(self, tile):
        choices = ['up', 'right', 'down', 'left']
        ran = random.choice(choices)
        row = tile.row
        col = tile.col
        match ran:
            case 'up':
                print("up")
                if row == 0:
                    return

                self.current_tile = self.data[row - 1][col]
                print("current tile move - col", self.current_tile.col, "row", self.current_tile.row)
                self.current_tile.value = 'p'

            case 'right':
                print("right")
                if col == self.width - 1:
                    return

                self.current_tile = self.data[row][col + 1]
                print("current tile move - col", self.current_tile.col, "row", self.current_tile.row)
                self.current_tile.value = 'p'

            case 'down':
                print("down")
                if row == self.height - 1:
                    return

                self.current_tile = self.data[row+1][col]
                print("current tile move - col", self.current_tile.col, "row", self.current_tile.row)
                self.current_tile.value = 'p'

            case 'left':
                print("left")
                if col == 0:
                    return

                self.current_tile = self.data[row][col-1]
                print("current tile move - col", self.current_tile.col, "row", self.current_tile.row)
                self.current_tile.value = 'p'


gridSize = 4
row = random.randint(0, gridSize - 1)
col = random.randint(0, gridSize - 1)
grid = Grid(gridSize, gridSize, (col, row), 'w')

# pick a random starting point for the walk, I can make this a fixed starting point later if I want

print("starting point is col", grid.current_tile.col, "row", grid.current_tile.row)

if grid.get(col, row).value == 'w':
    grid.set(col, row, 'p')

grid.printGrid()

for i in range(10):
    grid.move(grid.current_tile)
    grid.printGrid()
