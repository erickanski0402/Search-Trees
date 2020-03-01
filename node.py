from board import Board

class Node:
    def __init__(self, boardStr):
        self.boardStr = boardStr
        self.neighbors = {}
        pass

    def __str__(self, level=0):
        ret = "\t"*level+repr(self.boardStr)+"\n"
        for child in self.neighbors.values():
            ret += child.__str__(level+1)
        return ret

    def resolveNeighbors(self):
        board = Board(self.boardStr)
        self.neighbors = self.convertNeighborsToNodes(board.getNeighbors())
        pass

    def convertNeighborsToNodes(self, neighbors):
        map = {}
        for key in neighbors:
            map[key] = Node(neighbors.get(key))
        return map
