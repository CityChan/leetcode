class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        def dfs(board, c1, c2):
            if c1<0 or c2<0 or c1>=len(board) or c2>=len(board[0]):
                return
            if board[c1][c2]=='E':
                count=0
                for i in [-1,0,1]:
                    for j in [-1, 0, 1]:
                        if i!=0 or j!=0:
                            if len(board)>c1+i>=0 and len(board[0])>c2+j>=0:
                                count+=(1 if board[c1+i][c2+j]!='M' else 0)
                            else:
                                count+=1

                if count==8:
                    board[c1][c2]='B'
                    for i in [-1,0,1]:
                        for j in [-1, 0, 1]:
                            if i!=0 or j!=0:
                                dfs(board, c1+i, c2+j)
                else:
                    board[c1][c2]=str(8-count)
            # elif board[c1][c2]=='M':
            #     board[c1][c2]=='X'
            #     return 'X'
                
        
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        else:
            dfs(board,click[0],click[1])
            
            
        return board
        
