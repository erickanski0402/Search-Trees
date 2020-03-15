from helpers import matrixToStr, strToMatrix, strToIntArray
from constants import DIRECTION_LIST, UP, DOWN, LEFT, RIGHT, GOAL_STATE_MAP
import numpy as np

class Board:
    def __init__(self, boardStr):
        self.boardStr = boardStr
        self.matrix = strToMatrix(boardStr)
        pass

    def copyMatrix(self):
        return self.matrix.copy()

    def swapValues(self, val, oldPos, newPos):
        mat = self.copyMatrix()
        mat[oldPos[0], oldPos[1]] = val
        mat[newPos[0], newPos[1]] = 0
        return mat

    def getNeighbors(self):
        map = {}
        for dir in DIRECTION_LIST:
            matrix = self.move(dir)
            if matrix is not None:
                map[dir] = matrixToStr(matrix)
            continue
        return map

    def move(self, dir):
        pos = self.findEmptySpace()

        if dir == UP and pos[0] > 0:
            # move up
            return self.up(pos)
        elif dir == DOWN and pos[0] < 2:
            # move down
            return self.down(pos)
        elif dir == LEFT and pos[1] > 0:
            # move left
            return self.left(pos)
        elif dir == RIGHT and pos[1] < 2:
            # move right
            return self.right(pos)
        return None

    def up(self, oldPos):
        newPos = [oldPos[0] - 1, oldPos[1]]
        temp = self.matrix.item((newPos[0], newPos[1]))
        return self.swapValues(temp, oldPos, newPos)

    def down(self, oldPos):
        newPos = [oldPos[0] + 1, oldPos[1]]
        temp = self.matrix.item((newPos[0], newPos[1]))
        return self.swapValues(temp, oldPos, newPos)

    def left(self, oldPos):
        newPos = [oldPos[0], oldPos[1] - 1]
        temp = self.matrix.item((newPos[0], newPos[1]))
        return self.swapValues(temp, oldPos, newPos)

    def right(self, oldPos):
        newPos = [oldPos[0], oldPos[1] + 1]
        temp = self.matrix.item((newPos[0], newPos[1]))
        return self.swapValues(temp, oldPos, newPos)

    def findEmptySpace(self):
        return np.argwhere(self.matrix == 0)[0]
