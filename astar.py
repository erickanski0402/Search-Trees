from helpers import calculateManhattanDistance, deleteFromMap, getFirstNeighbor
from board import Board
from queue import PriorityQueue

def aStarSearch(root, goal):
    # Seconday value to determine priority when 2+ nodes share a manhattan distance (MD)
    secondaryPriority = 0
    # 'Heap' is instantiated
    heap = PriorityQueue()
    # Inserts the root into the queue with the MD as its first priorty
    heap.put((calculateManhattanDistance(root.boardStr), secondaryPriority, root))
    # Frontier instantiated and root is added
    frontier = {}
    frontier[root.boardStr] = True
    # Explored set to empty map, expanded nodes and max_search_depth initilized
    explored = {}
    expandedNodes = 0
    max_search_depth = 0
    # While the heap/priorty queue is not empty
    while heap.qsize() > 0:
        # Pulls the next node out of the queue
        state = heap.get()[2]
        # Adds node string to set of explored values
        board = state.boardStr
        explored[board] = True
        # Removes board string from frontier
        deleteFromMap(frontier, board)
        # if board is found to be the goal state
        if board == goal:
            print("SOLUTION FOUND!!!!!!!!!! (Airhorn noises)")
            # Return solution and relevant information
            return (state.getPathToRoot(), max_search_depth, expandedNodes)
        # Gets all possible neighbor boards for current states
        neighbors = state.resolveNeighbors(state.height)
        expandedNodes += 1
        # For every neighbor generated
        for key in neighbors.keys():
            cleanupList = []
            neighbor = neighbors.get(key)
            str = neighbor.boardStr
            # if the neighbor is not already set to be explored or hasnt been explored prior
            if not (frontier.get(str) or explored.get(str)):
                # Secondary priority incremented
                secondaryPriority += 1
                # Neighbor is added to the queue
                heap.put((calculateManhattanDistance(neighbor.boardStr), secondaryPriority, neighbor))
                frontier[str] = True
            else:
                # Otherwise the neighbor is set to be pruned from the node's list of neighbors
                cleanupList.append(key)
            continue
        # Prunes redundant nodes
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
