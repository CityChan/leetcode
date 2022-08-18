class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(grid, i, j, d):
            if 0<=i<len(grid) and 0<=j<len(grid[0]):
                if grid[i][j]==1:
                    
                    path=d
                    # print(path)
                    grid[i][j]=0
                    path+=dfs(grid, i-1, j, 'u')
                    # print(path)
                    path+=dfs(grid, i+1, j, 'd')
                    # print(path)
                    path+=dfs(grid, i, j-1, 'l')
                    # print(path)
                    path+=dfs(grid, i, j+1, 'r')
                    # print(path)
                    path+="b"
                    
                    return path
            return ""
        total_path = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    # path = ""
                    
                    total_path.add(dfs(grid, i, j, 'o'))
        # print(set([dfs(grid, i, j, 'o') for i in range(len(grid)) for j in range(len(grid[0]))]))
        return len(total_path)
        
