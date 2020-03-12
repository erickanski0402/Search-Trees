from bfs import breadthFirstSearch
from dfs import depthFirstSearch
from astar import aStarSearch
from constants import GOAL_STATE
from node import Node
from timeit import default_timer
import sys

# RUN WITH:
# python driver.py bfs 3,1,2,0,4,5,6,7,8
# python driver.py bfs 1,2,5,3,4,0,6,7,8
start = default_timer()
alg = sys.argv[1]
boardStr = sys.argv[2]
root = Node(boardStr, None)

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
    algOutput = breadthFirstSearch(root, GOAL_STATE)
    pass
elif alg == 'dfs':
    algOutput = depthFirstSearch(root, GOAL_STATE)
    pass
elif alg == 'ast':
    algOutput = aStarSearch(root, GOAL_STATE)
    pass
else:
    print('Argument unknown')

output['path_to_goal'], output['max_search'], output['nodes_expanded'] = algOutput
output['cost_of_path'] = len(output['path_to_goal'])
output['search_depth'] = len(output['path_to_goal'])
output['running_time'] = round(default_timer() - start, 10)
# output['max_ram_usage'] = resource.ru_maxrss

for key in output.keys():
    print(f'{key}:', output[key])
# print('Solution found:      ', output['path_to_goal'])
# print('Solution found:      ', output['path_to_goal'])
# print('Max Depth of Tree:   ', output['max_search'])
# print('Nodes Expanded:      ', output['nodes_expanded'])
# print('Total runtime:       ', output['running_time'])
# print('Tree:')
# str(root)
# print(root)
# print('Moves from initial:  ', list(algOutput.values())[1:])
# Stream output of methods to 'output.txt'
