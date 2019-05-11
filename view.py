import model
import os

class view:
    @staticmethod
    def printMap(theModel):
        clear = lambda: os.system('cls')
        clear()
        print("", end=" ")
        for i in range(theModel.rows):
            print("_", end="")
        print("")
        for j in range(theModel.cols - 1, -1, -1):
            print("|", end=" ")
            for i in range(theModel.rows):
                isSnake = False
                for elm in theModel.snake:
                    if (elm.x == i and elm.y == j):
                        isSnake = True
                if isSnake:
                    print("◙", end=" ") 
                elif theModel.grid[i][j] == model.cell.food:
                    print("X", end=" ")
                else:
                    print(" ", end=" ")
            print(" |")
        for i in range(theModel.rows):
            print("_", end="")
        print("")