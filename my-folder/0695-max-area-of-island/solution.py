class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
                return 0
            else:
                now_count=1
                grid[i][j]=0
                now_count+=dfs(grid, i-1, j)
                now_count+=dfs(grid, i+1, j)
                now_count+=dfs(grid, i, j-1)
                now_count+=dfs(grid, i, j+1)
            return now_count
                
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:                
                    max_area = max(max_area, dfs(grid, i, j))
        
        
        return max_area
        
