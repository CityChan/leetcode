class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sb = []
                    self.dfs(grid,i,j,sb,0)
                    islands.add(tuple(sb))
        return len(islands)
        
    def dfs(self, grid, i,j, sb,d):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >=n:
            return 
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        sb.append(d)
        self.dfs(grid, i+1, j, sb, 1)
        self.dfs(grid, i-1, j, sb, 2)
        self.dfs(grid, i, j+1, sb, 3)
        self.dfs(grid, i, j-1, sb, 4)
        sb.append(-d)
        
