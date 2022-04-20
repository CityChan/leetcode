class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        if m==1 or n==1:
            return board
            
        to_iter = []
        for i in range(n):
            if board[0][i]=='O':
                to_iter.append((0, i))
            if board[m-1][i]=='O':
                to_iter.append((m-1, i))
        for j in range(1, m-1):              
            if board[j][0]=='O':
                to_iter.append((j, 0))
            if board[j][n-1]=='O':
                to_iter.append((j, n-1))
                
        def dfs(board, i, j):
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j]='S'
                dfs(board, i-1, j)
                dfs(board, i+1, j)
                dfs(board, i, j-1)
                dfs(board, i, j+1)
                
        for i, j in to_iter:
            dfs(board, i, j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j]=='S':
                    board[i][j]='O'
                else:
                    board[i][j]='X'

            
        

            
        
