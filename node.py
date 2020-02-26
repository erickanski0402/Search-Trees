class Node:
    def __init__(self, board):
        self.board = board
        self.neigbors = board.generateNeighbors()
        pass
