from helpers import strToMatrix, matrixToStr
from constants import GOAL_STATE
from board import Board
from collections import deque

def depthFirstSearch(initState):
    # frontier is initialized to a stack with the first board
    stack = deque()
    stack.append(initState)

    frontier = {}
    frontier[matrixToStr(initState.matrix)] = True

    # explored is initialized as an empty set
    explored = {}

    # while frontier is not empty
    while len(stack) > 0:
        # current state is set to the board at the top of the set
        state = stack.pop()

        # current state is added to the set of explored boards
        explored[matrixToStr(state.matrix)] = state.dirFromParent

        # if current state is GOAL_STATE
        if matrixToStr(state.matrix) == GOAL_STATE:
            # Return SUCCESS
            print("SOLUTION FOUND!!!!!!!!!! (Airhorn noises)")
            return explored

        tempList = []
        # for every neighbor of the current state board
        for neighbor in state.getNeighbors():
            str = matrixToStr(neighbor.matrix)
            # if neighbor is not in the frontier or in explored
            if not frontier.get(str) and not explored.get(str):
                # add neighbor to the frontier queue (ensure neighbors are queued in UDLR order)
                tempList.append(neighbor)

        tempList.reverse()
        # frontier.append(_) for _ in tempList if _ is not None
        for _ in tempList:
            stack.append(_)
        pass
    return []
