class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        self.visited = [[0 for _ in range(n)] for _ in range(n)]
        self.cnt = Counter()
        root = 0
        self.dir = [[0,1], [1,0], [0,-1], [-1,0]]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and self.visited[i][j] == 0:
                    root += 1
                    self.dfs(grid, i,j, root)
        ans = max(self.cnt.values() or [0])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    s = set()
                    for a,b in self.dir:
                        x,y = i + a , j + b
                        if x >= 0 and x < n and y >= 0 and y < n:
                            s.add(self.visited[x][y])
                    ans = max(ans, sum([self.cnt[root] for root in s]) + 1)
        return ans


    def dfs(self, grid, i, j, root):
        n = len(grid)
        self.visited[i][j] = root
        self.cnt[root] += 1
        for d in self.dir:
            x, y = i + d[0], j + d[1]
            if x >= 0 and x < n and y >= 0 and y < n and grid[x][y] == 1 and self.visited[x][y] == 0:
                self.dfs(grid, x,y, root)
        

