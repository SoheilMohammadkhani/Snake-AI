import view
import model
import time
import keyboard
import threading
import os
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
from msvcrt import getch

class Indivitual:
    value = Sequential()
    fitness = 0
    def __init__(self, val):
        self.value = val
    def fitnessPow2(self):
        return self.fitness * self.fitness

pool = []

popSize = 100

m = model.model(10, 10)

move = False
not_Lose = True

chengeColor = lambda: os.system('color 04')
chengeColor()

def createSnakeModel():
    snakeModel = keras.models.Sequential()
    snakeModel.add(Dense(units=4))
    snakeModel.add(Activation("sigmoid"))
    snakeModel.add(Dense(units=3))
    snakeModel.add(Activation("sigmoid"))
    return snakeModel

def createPop():
    global pool
    for i in range(popSize):
        tmpIndivitual = Indivitual(createSnakeModel())
        pool.append(tmpIndivitual)

'''
 Main Func
'''

createPop()

print(popSize)

print(len(pool))
