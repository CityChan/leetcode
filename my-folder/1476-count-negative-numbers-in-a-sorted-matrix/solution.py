class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r = m-1
        c = 0
        count = 0
        
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                count += n - c
                r -= 1
            else:
                c += 1
        
        return count
