import view
import model
import time
import keyboard
import threading
import os
from msvcrt import getch

m = model.model(10, 10)

move = False
not_Lose = True

chengeColor = lambda: os.system('color 04')
chengeColor()

def normalMove():
    global not_Lose
    while not_Lose:
        m.nextMove(model.direction.null)
        time.sleep(0.25);   
        view.view.printMap(m)
        if m.checkLose():
            not_Lose = False
            

def keyboardMove():
    global not_Lose
    while not_Lose:
        key = ord(getch())
        if key == 224:
            key = ord(getch())
            if key == 80:
                m.nextMove(model.direction.down)
            elif key == 72:
                m.nextMove(model.direction.up)
            elif key == 75:
                m.nextMove(model.direction.left) 
            elif key == 77:
                m.nextMove(model.direction.right) 
            
            time.sleep(0.25);   
            view.view.printMap(m)

            if m.checkLose():
                not_Lose = False

threading.Thread(target = normalMove).start()
threading.Thread(target = keyboardMove).start()

print("end")
