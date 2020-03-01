class Output:
    def __init__(self,
                path_to_goal,
                cost_of_path,
                nodes_expanded,
                search_depth,
                max_search_depth,
                running_time,
                max_ram_usage):
        self.path_to_goal = path_to_goal
        self.cost_of_path = cost_of_path
        self.nodes_expanded = nodes_expanded
        self.search_depth = search_depth
        self.max_search_depth = max_search_depth
        self.running_time = running_time
        self.max_ram_usage = max_ram_usage
        pass

    def outputToTxtFile(self):
        pass

    def setPathToGoal(self, path_to_goal):
        self.path_to_goal = path_to_goal

    def setCostOfPath(self, cost_of_path):
        self.cost_of_path = cost_of_path

    def setNodesExpanded(self, nodes_expanded):
        self.nodes_expanded = nodes_expanded

    def setSearchDepth(self, search_depth):
        self.search_depth = search_depth

    def setMaxSearchDepth(self, max_search_depth):
        self.max_search_depth = max_search_depth

    def setRunningTime(self, running_time):
        self.running_time = running_time

    def setMaxRamUsage(self, max_ram_usage):
        self.max_ram_usage = max_ram_usage
