class Solution:
    class Edge:
        def __init__(self, node: str, weight: float):
            self.node = node
            self.weight = weight

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            equation = equations[i]
            a, b = equation[0], equation[1]
            w = values[i]
            if a not in graph:
                graph[a] = []
            graph[a].append(self.Edge(b, w))
            if b not in graph:
                graph[b] = []
            graph[b].append(self.Edge(a, 1.0/w))

        res = [0.0] * len(queries)
        for i in range(len(queries)):
            query = queries[i]
            start, end = query[0], query[1]
            res[i] = self.bfs(graph, start, end)
        return res


    def bfs(self, graph, start, end):
        if start not in graph or end not in graph:
            return -1.0
        if start == end:
            return 1.0
        
        queue = collections.deque([start])
        visited = set([start])
        weight = {start: 1.0}
        while queue:
            cur = queue.popleft()
            for neighbor in graph[cur]:
                if neighbor.node in visited:
                    continue
                weight[neighbor.node] = weight[cur] * neighbor.weight
                if neighbor.node == end:
                    return weight[end]
                visited.add(neighbor.node)
                queue.append(neighbor.node)
        return -1.0

