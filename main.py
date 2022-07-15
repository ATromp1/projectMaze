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
    def __init__(self, width, height, value=''):
        self.width = width
        self.height = height
        self.direction = None
        self.data = np.ndarray(shape=(width, height), dtype=Tile)
        for col in range(height):
            for row in range(width):
                self.data[row][col] = Tile(col, row, value)

        self.history = [np.random.choice(self.data.ravel())]

        #set starting point value
        self.history[0].value = 'p'
        # second starting point
        np.random.choice(self.data.ravel()).value = 'x'




    def set(self, col, row, value):
        self.data[col][row].value = value

    def get(self, col, row):
        return self.data[col][row]

    def printGrid(self):
        print(self.data)

    def get_next_tile(self):
        tile = self.history[-1]
        direction = self.pick_direction(tile)
        row = tile.row
        col = tile.col
        print(direction)
        match direction:
            case 'up':
                self.direction = direction
                return self.data[row - 1][col]

            case 'right':
                self.direction = direction
                return self.data[row][col + 1]

            case 'down':
                self.direction = direction
                return self.data[row + 1][col]

            case 'left':
                self.direction = direction
                return self.data[row][col - 1]

    def move(self, next_tile):
        self.check_loop(next_tile)
        self.history.append(next_tile)
        self.history[-1].value = 'p'

    def pick_direction(self, tile):
        direction = ['up', 'down', 'left', 'right']
        if tile.row == 0:
            direction = ['right', 'down', 'left']
            if tile.col == self.width - 1:
                direction = ['down', 'left']
            if tile.col == 0:
                direction = ['down', 'right']
        elif tile.row == self.height - 1:
            direction = ['up', 'right', 'left']
            if tile.col == self.width - 1:
                direction = ['up', 'left']
            if tile.col == 0:
                direction = ['up', 'right']
        elif tile.col == self.width - 1:
            direction = ['up', 'down', 'left']
        elif tile.col == 0:
            direction = ['up', 'right', 'down']

        match self.direction:
            case 'up':
                direction.remove('down')
            case 'down':
                direction.remove('up')
            case 'left':
                direction.remove('right')
            case 'right':
                direction.remove('left')
        return random.choice(direction)

    def check_loop(self, next_tile):
        if next_tile.value == 'p':
            # print(self.history.index(next_tile))
            x = np.where(self.data == next_tile)
            # print("Grid index next tile", x)
            # print("Which is:", self.data[x].tolist()[0].col, self.data[x].tolist()[0].row, self.data[x].tolist()[0].value)
            history_index = self.history.index(self.data[x])
            for element in reversed(self.history[history_index + 1:]):
                self.data[element.row][element.col].value = 'w'
            self.history = self.history[:history_index + 1]

    def walk_path(self):
        while True:
            next_tile = self.get_next_tile()
            if next_tile.value == 'x':
                self.move(next_tile)
                self.printGrid()
                break
            self.move(next_tile)
            self.printGrid()


gridSize = 6
grid = Grid(gridSize, gridSize, 'w')
grid.printGrid()
grid.walk_path()
