class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n = len(rooms), len(rooms[0])
        q = deque([(i, j ) for i in range(m) for j in range(n) if rooms[i][j] == 0])
        d = 0
        INF = 2**31 -1
        while q:
            d += 1
            for _ in range(len(q)):
             i, j  = q.popleft()
             for a, b in [[0,1], [1,0], [0, -1], [-1, 0]]:
                x, y = a + i, b + j
                if 0<= x <m and 0<= y < n and rooms[x][y] == INF:
                     rooms[x][y] = d
                     q.append((x,y))
