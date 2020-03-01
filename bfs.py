from helpers import strToMatrix, matrixToStr, deleteFromMap
from constants import GOAL_STATE
from board import Board
from queue import Queue

def breadthFirstSearch(root):
    # Place the root node on the queue
    queue = Queue()
    queue.put(root)
    # Initialize empty frontier
    frontier = {}
    frontier[root.boardStr] = True
    # Initialize empty set of explored boards
    explored = {}

    while queue.qsize() > 0:
        # Pop the next board node off the queue
        state = queue.get()
        # Add board to the explored map and remove it from frontier map
        board = state.boardStr
        explored[board] = True
        deleteFromMap(frontier, board)

        # if the board is equal to the goal state
        if board  == GOAL_STATE:
            print("SOLUTION FOUND!!!!!!!!!! (Airhorn noises)")
            return explored

        # Adds neighbors to the current node
        state.resolveNeighbors()
        neighbors = state.neighbors
        # Iterates over all the neighbors of the current node
        for key in neighbors.keys():
            str = neighbors.get(key)
            # if the current neighbor hasnt already been explored and isnt in  queue to be
            if not (frontier.get(str) or explored.get(str)):
                # Put the board in queue to be explored
                queue.put(neighbors.get(key))
                frontier[str] = True
            else:
                # Otherwise prune the redundant neighbor from the tree
                del neighbors[key]
            pass
        pass
    return explored

# def breadthFirstSearch(initState):
#     # Queue initialized with the first board
#     queue = Queue()
#     queue.put(initState)
#     nodes_expanded = 0
#
#     frontier = {}
#     frontier[matrixToStr(initState.matrix)] = True
#
#     # Explored: empty set
#     explored = {}
#
#     # while frontier is NOT empty
#     while queue.qsize() > 0:
#         # current state is te next item in frontier queue
#         state = queue.get()
#
#         # add current state to set of explored boards
#         explored[matrixToStr(state.matrix)] = state.dirFromParent
#
#         # if current state is GOAL_STATE
#         if matrixToStr(state.matrix) == GOAL_STATE:
#             # Return SUCCESS
#             print("SOLUTION FOUND!!!!!!!!!! (Airhorn noises)")
#             return explored
#
#         # for every neighbor of the current state board
#         neighbors = state.getNeighbors()
#         for key in neighbors.keys():
#             str = matrixToStr(neighbors[key].matrix)
#             # if neighbor is not in the frontier or in explored
#             if not frontier.get(str) and not explored.get(str):
#                 # add neighbor to the frontier queue (ensure neighbors are queued in UDLR order)
#                 queue.put(neighbors[key])
#         pass
#     return []
