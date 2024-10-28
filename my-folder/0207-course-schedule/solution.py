class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        grid = [[] for _ in range(numCourses)]
        for t,s in prerequisites:
            grid[s].append(t)
        self.onPath = [False for _ in range(numCourses)]
        self.visited = [False for _ in range(numCourses)]
        self.hasCycle = False
        for i in range(numCourses):
            self.traverse(grid, i)
        return not self.hasCycle

    def traverse(self, grid, s):
        if self.onPath[s]:
            self.hasCycle = True
        if self.visited[s] or self.hasCycle:
            return    
        self.visited[s] = True
        self.onPath[s] = True
        for t in grid[s]:
            self.traverse(grid, t)
        self.onPath[s] = False
