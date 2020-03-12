from helpers import getKeyByValue, strToMatrix
from board import Board

class Node:
    def __init__(self, boardStr, parent):
        self.boardStr = boardStr
        self.parent = parent
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
            map[key] = Node(neighbors.get(key), self)
        return map

    def getPathToRoot(self):
        # Starting with the given node
        current = self
        path = []
        # until there are no more parent nodes to search through
        while current.parent is not None:
            # Get the boardStr of current node
            str = current.boardStr
            # Move current node to look at the next parent
            current = current.parent
            # Look at the neighbor nodes of the new current node and append the key that corresponds to the given string
            path.append(getKeyByValue(Board(current.boardStr).getNeighbors(), str)) # Eugh.
        # Final array will be in order of goalNode->root, and thus needs to be reversed
        path.reverse()
        return path

    def findMaxDepth(root):
        return 0
