import numpy as np

class Board:
    def __init__(self, boardStr):
        self.boardStr = boardStr
        self.matrix = np.array([int(i) for i in boardStr.split(',') ]).reshape(3,3)
        pass

    def copyMatrix(self):
        return self.matrix.copy()

    def matrixToStr(self):
        # flattens matrix into 1-D, converts np array to list, converts each item from int->str, join each item on ','
        return ','.join([str(_) for _ in self.matrix.flatten().tolist()])

    def swapValues(self, val, oldPos, newPos):
        mat = self.copyMatrix()
        mat[oldPos[0], oldPos[1]] = val
        mat[newPos[0], newPos[1]] = 0
        return mat

    def generateNeighbors(self):
        arr = [self.move('U'), self.move('D'), self.move('L'), self.move('R')]
        return [i for i in arr if i is not None]

    def move(self, dir):
        pos = self.findEmptySpace()

        if dir == 'U' and pos[0] > 0:
            # move up
            return self.up(pos)
        elif dir == 'D' and pos[0] < 2:
            # move down
            return self.down(pos)
        elif dir == 'L' and pos[1] > 0:
            # move left
            return self.left(pos)
        elif dir == 'R' and pos[1] < 2:
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
