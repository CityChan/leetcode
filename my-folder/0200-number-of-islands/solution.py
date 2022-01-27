class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        def search_p(grid, i, j):
            if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    for ii, jj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        search_p(grid, i+ii, j+jj)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count +=1
                    search_p(grid, i, j)
        return count
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def search_p(grid, i, j, m, n):
#             grid[i][j]="2"
#             for aa, bb in ((-1, 0), (1, 0), (0, 1), (0, -1)):
#                 ii, jj = i+aa, j+bb
#                 if ii>=0 and ii<m and jj>=0 and jj<n and grid[ii][jj]=="1":
#                     search_p(grid, ii, jj, m, n)
                    
#         c = 0
#         m = len(grid)
#         n = len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]=="1":
#                     search_p(grid, i, j, m, n)
#                     c+=1
#         return c
        
        
        
