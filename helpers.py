import numpy as np

def strToMatrix(str):
    # splits the string in to a list by ',' characters, casts them to ints before convering the list into a 3x3 numpy matrix
    return np.array([int(i) for i in str.split(',') ]).reshape(3,3)

def matrixToStr(matrix):
    # flattens matrix into 1-D, converts np array to list, converts each item from int->str, join each item on ','
    return ','.join([str(_) for _ in matrix.flatten().tolist()])

def deleteFromMap(map, key):
    if map.get(key):
        del map[key]
