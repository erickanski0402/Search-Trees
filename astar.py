from helpers import calculateManhattanDistance, deleteFromMap
from board import Board
from queue import PriorityQueue

def aStarSearch(root, goal):
    secondaryPriority = 0
    heap = PriorityQueue()
    heap.put((calculateManhattanDistance(root.boardStr), secondaryPriority, root))

    frontier = {}
    frontier[root.boardStr] = True

    explored = {}
    expandedNodes = 0

    while heap.qsize() > 0:
        state = heap.get()[2]

        board = state.boardStr
        explored[board] = True
        deleteFromMap(frontier, board)

        if board == goal:
            print("SOLUTION FOUND!!!!!!!!!! (Airhorn noises)")
            # return tuple of (Path to root, max node depth, nodes expanded)
            return (state.getPathToRoot(), root.findMaxDepth(), expandedNodes)

        neighbors = state.resolveNeighbors()
        expandedNodes += 1

        for key in neighbors.keys():
            cleanupList = []
            neighbor = neighbors.get(key)
            str = neighbor.boardStr

            if not (frontier.get(str) or explored.get(str)):

                secondaryPriority += 1
                heap.put((calculateManhattanDistance(neighbor.boardStr), secondaryPriority, neighbor))
                frontier[str] = True
            else:

                cleanupList.append(key)
            continue

        for _ in cleanupList:
            deleteFromMap(neighbors, _)
            continue
        continue
    return ()
