class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def search_p(grid, i, j, m, n):
            grid[i][j]="2"
            for aa, bb in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ii, jj = i+aa, j+bb
                if ii>=0 and ii<m and jj>=0 and jj<n and grid[ii][jj]=="1":
                    search_p(grid, ii, jj, m, n)
                    
        c = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    search_p(grid, i, j, m, n)
                    c+=1
        return c
        
        
        
