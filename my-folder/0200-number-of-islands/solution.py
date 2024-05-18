class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    q = [(i, j)]
                    while q:
                        ii, jj = q.pop(0)
                        if 0<=ii<len(grid) and 0<=jj<len(grid[0]):
                            if grid[ii][jj]=="1":
                                grid[ii][jj]="0"
                                q.extend([(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)])
                    count+=1
        return count
                    
        
