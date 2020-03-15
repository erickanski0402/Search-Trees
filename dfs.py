from helpers import deleteFromMap, getFirstNeighbor
from board import Board
from collections import deque

def depthFirstSearch(root, goal):
    # Place the root node on the queue
    stack = []
    stack.append(root)
    # Initialize empty frontier
    frontier = {}
    frontier[root.boardStr] = True
    # Initialize empty set of explored boards
    explored = {}
    expandedNodes = 0
    max_search_depth = 0

    while len(stack) > 0:
        # Pop the next board node off the queue
        state = stack.pop()
        # Add board to the explored map and remove it from frontier map
        board = state.boardStr
        explored[board] = True
        deleteFromMap(frontier, board)
        # if the board is equal to the goal state
        if board == goal:
            print("SOLUTION FOUND!!!!!!!!!! (Airhorn noises)")
            return (state.getPathToRoot(), max_search_depth, expandedNodes)

        # Adds neighbors to the current node
        neighbors = state.resolveNeighbors(state.height)
        expandedNodes += 1

        # Iterates over all the neighbors of the current node
        cleanupList = []
        tempList = []
        for key in neighbors.keys():
            str = neighbors.get(key).boardStr
            # if the current neighbor hasnt already been explored and isnt in  queue to be
            if not (frontier.get(str) or explored.get(str)):
                # Put the board in queue to be explored
                tempList.append(neighbors.get(key))
                frontier[str] = True
            else:
                # Otherwise prune the redundant neighbor from the tree
                cleanupList.append(key)
            continue
        tempList.reverse()
        for _ in tempList:
            stack.append(_)
            continue
        for _ in cleanupList:
            deleteFromMap(neighbors, _)
            continue

        # Assuming neighbors are present, gets their height, otherwise 0
        search_depth = 0 if not bool(neighbors) else getFirstNeighbor(neighbors).height
        # If these nodes are found to be the deepest level of the tree
        if search_depth > max_search_depth:
            # A new max_search_depth is set
            max_search_depth = search_depth
        continue
    return ()
