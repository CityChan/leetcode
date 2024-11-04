class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ans = False
        self.word = word
        self.visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, 0)
                if self.ans:
                    return True
        return False

    def dfs(self, board, i, j, p):
        m,n = len(board), len(board[0])
        if p == len(self.word):
            self.ans = True
            return
        if self.ans:
            return 
        dirs = [[1,0], [0,1], [-1,0], [0,-1]]
        if i < 0 or i >= m or j < 0 or j >=n:
            return
        if self.visited[i][j] == True:
            return
        if board[i][j] != self.word[p]:
            return
        self.visited[i][j] = True
        for d in dirs:
            x, y = i + d[0], j + d[1]
            self.dfs(board,x,y,p+1)
        self.visited[i][j] = False
        return
