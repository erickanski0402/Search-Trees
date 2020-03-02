from helpers import strToMatrix, matrixToStr, deleteFromMap
from constants import GOAL_STATE
from board import Board
from collections import deque

def depthFirstSearch(root):
    # Place the root node on the queue
    stack = deque()
    stack.append(root)
    # Initialize empty frontier
    frontier = {}
    frontier[root.boardStr] = True
    # Initialize empty set of explored boards
    explored = {}

    while len(stack) > 0:
        # Pop the next board node off the queue
        state = stack.pop()
        # Add board to the explored map and remove it from frontier map
        board = state.boardStr
        explored[board] = True
        deleteFromMap(frontier, board)

        # if the board is equal to the goal state
        if board  == GOAL_STATE:
            print("SOLUTION FOUND!!!!!!!!!! (Airhorn noises)")
            return explored

        # Adds neighbors to the current node
        neighbors = state.resolveNeighbors()
        # Iterates over all the neighbors of the current node
        cleanupList = []
        for key in neighbors.keys():
            tempList = []
            str = neighbors.get(key).boardStr
            # if the current neighbor hasnt already been explored and isnt in  queue to be
            if not (frontier.get(str) or explored.get(str)):
                # Put the board in queue to be explored
                # queue.put(neighbors.get(key))
                tempList.append(neighbors.get(key))
                frontier[str] = True
            else:
                # Otherwise prune the redundant neighbor from the tree
                cleanupList.append(key)
            pass
            tempList.reverse()
            for _ in tempList:
                stack.append(_)
                continue
            continue
        for _ in cleanupList:
            deleteFromMap(neighbors, _)
        continue
    return explored

# def depthFirstSearch(initState):
#     # frontier is initialized to a stack with the first board
#     stack = deque()
#     stack.append(initState)
#
#     frontier = {}
#     frontier[matrixToStr(initState.matrix)] = True
#
#     # explored is initialized as an empty set
#     explored = {}
#
#     # while frontier is not empty
#     while len(stack) > 0:
#         # current state is set to the board at the top of the set
#         state = stack.pop()
#
#         # current state is added to the set of explored boards
#         explored[matrixToStr(state.matrix)] = state.dirFromParent
#
#         # if current state is GOAL_STATE
#         if matrixToStr(state.matrix) == GOAL_STATE:
#             # Return SUCCESS
#             print("SOLUTION FOUND!!!!!!!!!! (Airhorn noises)")
#             return explored
#
#         tempList = []
#         # for every neighbor of the current state board
#         for neighbor in state.getNeighbors():
#             str = matrixToStr(neighbor.matrix)
#             # if neighbor is not in the frontier or in explored
#             if not frontier.get(str) and not explored.get(str):
#                 # add neighbor to the frontier queue (ensure neighbors are queued in UDLR order)
#                 tempList.append(neighbor)
#
#         tempList.reverse()
#         # frontier.append(_) for _ in tempList if _ is not None
#         for _ in tempList:
#             stack.append(_)
#         pass
#     return []
