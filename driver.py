from bfs import breadthFirstSearch
from dfs import depthFirstSearch
from astar import aStarSearch
from constants import GOAL_STATE
from node import Node
from timeit import default_timer
# from resource import getrusage, RUSAGE_SELF
import sys

# RUN WITH:
# python driver.py bfs 3,1,2,0,4,5,6,7,8
# python driver.py bfs 1,2,5,3,4,0,6,7,8
start = default_timer()
alg = sys.argv[1]
boardStr = sys.argv[2]
root = Node(boardStr, None, 0)

output = {
    'path_to_goal': None,
    'cost_of_path': None,
    'nodes_expanded': None,
    'search_depth': None,
    'max_search_depth': None,
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

output['path_to_goal'], output['max_search_depth'], output['nodes_expanded'] = algOutput
output['cost_of_path'] = len(output['path_to_goal'])
output['search_depth'] = len(output['path_to_goal'])
output['running_time'] = round(default_timer() - start, 10)
# output['max_ram_usage'] = getrusage(RUSAGE_SELF).ru_maxrss / 1000000

f = open('output.txt', 'w+')
for key in output.keys():
    f.write(f'{key}: {output[key]},\n')
f.close()
# print('Tree:')
# str(root)
# print(root)
# Stream output of methods to 'output.txt'
