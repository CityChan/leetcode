class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.players = [[0 for _ in range(2*n + 2)],[0 for _ in range(2*n + 2)]]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        print('move')
        n = len(self.board)
        print(self.players[player-1])
        self.players[player-1][row] += 1
        self.players[player-1][col+n] += 1
        print(self.players[player-1])

        if row == col:
            print(1)
            self.players[player-1][2*n] += 1
        if row == n-1 - col:
            print(2)
            self.players[player-1][2*n+1] += 1
            print(self.players[player-1])

        if max(self.players[player-1]) == n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
