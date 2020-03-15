from helpers import getKeyByValue, strToMatrix
from board import Board

class Node:
    def __init__(self, boardStr, parent, height):
        self.boardStr = boardStr
        self.parent = parent
        self.height = height
        self.neighbors = {}
        pass

    # def __str__(self, level=0):
    #     # Calculates tabs depending on level
    #     str = "\t"*level + f"{self.boardStr}\n"
    #     # for all neighbors in given node
    #     for neighbor in self.neighbors.values():
    #         str += neighbor.__str__(level+1)
    #     return str

    def resolveNeighbors(self, parentHeight):
        board = Board(self.boardStr)
        self.neighbors = self.convertNeighborsToNodes(board.getNeighbors(), parentHeight)
        return self.neighbors

    def convertNeighborsToNodes(self, neighbors, parentHeight):
        map = {}
        for key in neighbors:
            map[key] = Node(neighbors.get(key), self, parentHeight + 1)
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
