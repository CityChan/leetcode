class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            ans = 0
            if visited[i][j] == 1:
                return
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    visited[i][j] = 1
                    ans = max(ans, dfs(x, y))
                    visited[i][j] = 0
            return ans + 1

        m, n = len(matrix), len(matrix[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        return max(dfs(i, j) for i in range(m) for j in range(n))
