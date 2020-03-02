from board import Board

class Node:
    def __init__(self, boardStr):
        self.boardStr = boardStr
        self.neighbors = {}
        pass

    def __str__(self, level=0):
        # Calculates tabs depending on level
        str = "\t"*level + f"{self.boardStr}\n"
        # for all neighbors in given node
        for neighbor in self.neighbors.values():
            str += neighbor.__str__(level+1)
        return str

    def resolveNeighbors(self):
        board = Board(self.boardStr)
        self.neighbors = self.convertNeighborsToNodes(board.getNeighbors())
        return self.neighbors

    def convertNeighborsToNodes(self, neighbors):
        map = {}
        for key in neighbors:
            map[key] = Node(neighbors.get(key))
        return map
