class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]* 2]*n
        for i in range(n):
            if i == 0:
                dp[0][0] = 0
                dp[0][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(-prices[i], dp[i-1][1])
        return dp[n-1][0]

