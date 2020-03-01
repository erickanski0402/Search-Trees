from helpers import strToMatrix, matrixToStr
from bfs import breadthFirstSearch
from dfs import depthFirstSearch
from ast import aStarSearch
from board import Board
from node import Node
from timeit import default_timer
import sys

# RUN WITH:
# python driver.py bfs 3,1,2,0,4,5,6,7,8
# python driver.py bfs 1,2,5,3,4,0,6,7,8
start = default_timer()
alg = sys.argv[1]
boardStr = sys.argv[2]
root = Node(boardStr)

output = {
    'path_to_goal': None,
    'cost_of_path': None,
    'nodes_expanded': None,
    'search_depth': None,
    'max_search': None,
    'running_time': None,
    'max_ram_usage': None
}

algOutput = None

if alg == 'bfs':
    algOutput = breadthFirstSearch(root)
    pass
elif alg == 'dfs':
    algOutput = depthFirstSearch(root)
    pass
elif alg == 'ast':
    algOutput = aStarSearch(root)
    pass
else:
    print('Argument unknown')

print('Total runtime:       ', round(default_timer() - start, 10))
print('Solution found:      ', algOutput)
print('Tree:')
str(root)
print(root)
# print('Moves from initial:  ', list(algOutput.values())[1:])
# Stream output of methods to 'output.txt'
