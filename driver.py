from bfs import breadthFirstSearch
from dfs import depthFirstSearch
from ast import aStarSearch
from board import Board
import sys

alg = sys.argv[1]
boardStr = sys.argv[2]

board = Board(boardStr)
print(board.matrix)
print(board.matrixToStr())

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
    algOutput = breadthFirstSearch(board)
    pass
elif alg == 'dfs':
    algOutput = depthFirstSearch(board)
    pass
elif alg == 'ast':
    algOutput = aStarSearch(board)
    pass
else:
    print('Argument unknown')

# Stream output of methods to 'output.txt'
