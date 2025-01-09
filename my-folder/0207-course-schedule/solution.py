class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grid = [[] for _ in range(numCourses)]
        for t,s in prerequisites:
            grid[s].append(t)
        self.path = [False for _ in range(numCourses)]
        self.visited = [False for _ in range(numCourses)]
        self.has_cycle = False
        for i in range(numCourses):
            self.traverse(grid, i)
        return not self.has_cycle

    def traverse(self, grid, i):
        if self.path[i]:
            self.has_cycle = True
        if self.visited[i] or self.has_cycle:
            return
        self.path[i] = True
        self.visited[i] = True
        for v in grid[i]:
            self.traverse(grid, v)
        self.path[i] = False

