class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        self.ans = False
        m,n = len(maze), len(maze[0])
        dirs = [[0,1], [1,0], [0,-1], [-1, 0]]

        q = deque([start])
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[start[0]][start[1]] = True

        while q:
            cur = q.popleft()
            for dir in dirs:
                x,y = cur[0], cur[1]
                while 0<=x<m and 0<=y<n and maze[x][y]==0:
                    x += dir[0]
                    y += dir[1]
                x -= dir[0]
                y -= dir[1]  
                if [x,y] == destination:
                    return True
                if not visited[x][y] == True:
                    visited[x][y] = True
                    q.append([x,y])
        return False
                    



            
