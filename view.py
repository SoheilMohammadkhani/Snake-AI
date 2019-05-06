import model
import os

class view:
    @staticmethod
    def printMap(theModel):
        clear = lambda: os.system('cls')
        clear()
        for j in range(theModel.cols - 1, -1, -1):
            for i in range(theModel.rows):
                isSnake = False
                for elm in theModel.snake:
                    if (elm.x == i and elm.y == j):
                        isSnake = True
                if isSnake:
                    print("◙", end="") 
                elif theModel.grid[i][j] == model.cell.food:
                    print("X", end="")
                else:
                    print("O", end="")
            print(" ")
                    