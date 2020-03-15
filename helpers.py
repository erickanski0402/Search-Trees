from constants import GOAL_STATE_MAP
import numpy as np

def strToMatrix(str):
    # splits the string in to a list by ',' characters, casts them to ints before convering the list into a 3x3 numpy matrix
    return np.array([int(i) for i in str.split(',') ]).reshape(3,3)

def matrixToStr(matrix):
    # flattens matrix into 1-D, converts np array to list, converts each item from int->str, join each item on ','
    return ','.join([str(_) for _ in matrix.flatten().tolist()])

def strToIntArray(str):
    return list(map(int, str.split(',')))

def getKeyByValue(map, val):
    for key in map.keys():
        if map.get(key) == val:
            return key
    raise Exception('Key/Value pair not found')

def deleteFromMap(map, key):
    if map.get(key):
        del map[key]

def calculateManhattanDistance(boardStr):
    totalDistance = 0
    matrix = strToMatrix(boardStr)
    for i in range(1,9):
        goalPos = GOAL_STATE_MAP.get(i)
        where = np.where(matrix == i)
        pos = (where[0][0], where[1][0])
        totalDistance += abs(goalPos[0] - pos[0]) + abs(goalPos[1] - pos[1])
        continue
    return totalDistance

def getFirstNeighbor(map):
    return map.get(next(iter(map)))
