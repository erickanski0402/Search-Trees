from constants import GOAL_STATE

def breadthFirstSearch(board):
    # Frontier: queue initialized with the first board
    # Explored: empty set

    # while frontier is NOT empty
        # current state is te next item in frontier queue
        # add current state to set of explored boards

        # if current state is GOAL_STATE
            # Return SUCCESS

        # for every neighbor of the current state board
            # if neighbor is not in the frontier or in explored
                # add neighbor to the frontier queue (ensure neighbors are queued in UDLR order)
    return "yo"
