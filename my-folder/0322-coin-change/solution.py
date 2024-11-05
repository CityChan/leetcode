class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [-666]*(amount + 1)
        return self.dp(coins, amount)
    
    def dp(self,coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if self.memo[amount] != -666:
            return self.memo[amount]
        res = float('inf')
        for coin in coins:
            if self.dp(coins,amount - coin) == -1:
                continue
            else:
                ans = self.dp(coins, amount - coin) + 1
                res = min(res, ans)
        self.memo[amount] = -1 if res == float('inf') else res
        return self.memo[amount] 
        

        

