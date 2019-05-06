import numpy as np
import random
import enum

class direction(enum.Enum):
    left = 0
    up = 1
    right = 2
    down = 3
    null = 4

class snakeCell:
    dir = direction.right
    x = 0
    y = 0
    def __init__(self, dir, x, y):
        self.x = x
        self.y = y
        self.dir = dir

class cell(enum.Enum):
    null = 0
    food = 1

class model:
    grid = None
    rows = 0
    cols = 0
    snake = []
    def __init__(self, rows, cols):
        self.grid = np.full((rows, cols), cell.null)
        self.rows = rows
        self.cols = cols
        self.snake.append(snakeCell(direction.right, 2, self.cols - 1))
        self.snake.append(snakeCell(direction.right, 1, self.cols - 1))
        self.snake.append(snakeCell(direction.right, 0, self.cols - 1))
    def nextMove(self, dirc = direction.null):
        if not (dirc == direction.null):
            self.snake[0].dir = dirc

        for elm in self.snake:
            if elm.dir == direction.left:
                if elm.x > 0:
                    elm.x -= 1
                else:
                    return False
            elif elm.dir == direction.up:
                if elm.y < self.cols - 1:
                    elm.y += 1
                else:
                    return False
            elif elm.dir == direction.right:
                if elm.x < self.rows - 1:
                    elm.x += 1
                else:
                    return False
            elif elm.dir == direction.down:
                if elm.y > 0:
                    elm.y -= 1
                else:
                    return False
                    
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].dir = self.snake[i - 1].dir
                

    def createFood(self):
        possibleCells = []
        for i in range(self.rows):
            for j in range(self.cols):
                isSnake = False
                for elm in self.snake:
                    if (elm.x == i and elm.y == j):
                        isSnake = True
                if not isSnake:
                    possibleCells.append([i, j])
        
        foodCell = random.choice(possibleCells)
        self.grid[foodCell[0]][foodCell[1]] = cell.food

        

