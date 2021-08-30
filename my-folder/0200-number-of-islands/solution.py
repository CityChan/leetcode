class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dp(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) :
                return
            if grid[i][j]=='1':
                grid[i][j]='#'
            else:
                return
            dp(grid, i+1, j)
            dp(grid, i-1, j)
            dp(grid, i, j+1)
            dp(grid, i, j-1)
            return
        
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    dp(grid, i, j)
                    c+=1
        return c
                
        
