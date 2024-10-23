class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [[1,0], [0,1], [-1, 0], [0, -1]]
        def dps(grid, i, j):
            visited[i][j] = 1
            grid[i][j] = '0'
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if visited[x][y] == 0 and grid[x][y] == '1':
                    dps(grid, x,y)
        ans = 0
        for k in range(m):
            for l in range(n):
                if k < 0 or k >= m or l < 0 or l >= n or grid[k][l] == '0':
                    continue
                ans +=1
                dps(grid, k, l)
        return ans


