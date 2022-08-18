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
                area[0]+=1
                grid[i][j]=0
                dfs(grid, i-1, j)
                dfs(grid, i+1, j)
                dfs(grid, i, j-1)
                dfs(grid, i, j+1)
            # return now_count+1
                
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area=[0]
                if grid[i][j]==1:    
                    dfs(grid, i, j)
                    max_area = max(max_area, area[0])
        
        
        return max_area
        
