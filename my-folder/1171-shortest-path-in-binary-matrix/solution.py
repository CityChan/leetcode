class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        n = len(grid)
        grid[0][0] = 1
        q = deque([(0, 0)])
        ans = 1
        dirs = [[0,1],[1,0],[1,1],[0,-1],[-1,0],[-1,-1],[1,-1],[-1,1]]
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                if i == j == n - 1:
                    return ans
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        q.append((x, y))
                        grid[x][y] = 1
            ans += 1
        return -1
            


            
            
            
        

