class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i,j)
        return res
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
            return 
        grid[i][j] = "0"
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        for d in dirs:
            x, y = i + d[0], j + d[1]
            self.dfs(grid, x, y)
        
