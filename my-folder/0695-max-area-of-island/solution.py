class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # count = 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area = 0
                    # count+=1
                    grid[i][j]=0
                    q = [(i, j)]
                    while q:
                        ii, jj = q.pop(0)
                        area+=1
                        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
       
                            nxt_i = ii+di
                            nxt_j = jj+dj
         
                            if 0<=nxt_i<len(grid) and 0<=nxt_j<len(grid[0]) and grid[nxt_i][nxt_j]==1:
                                # area+=1
                                grid[nxt_i][nxt_j]=0
                                q.append((nxt_i, nxt_j))
                    max_area = max(max_area, area)
        
        
        return max_area
        
