class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # count = 0
        # def search_p(grid, i, j):
        #     if i>=0 and i<len(grid) and j>=0 and j<len(grid[0]) and grid[i][j] == '1':
        #             grid[i][j] = '0'
        #             for ii, jj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        #                 search_p(grid, i+ii, j+jj)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == '1':
        #             count +=1
        #             search_p(grid, i, j)
        # return count
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    grid[i][j]='0'
                    q = [(i, j)]
                    while q:

                        ii, jj = q.pop(0)
                        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
       
                            nxt_i = ii+di
                            nxt_j = jj+dj
         
                            if 0<=nxt_i<len(grid) and 0<=nxt_j<len(grid[0]) and grid[nxt_i][nxt_j]=='1':
        
                                grid[nxt_i][nxt_j]='0'
                                q.append((nxt_i, nxt_j))
      
        return count
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
