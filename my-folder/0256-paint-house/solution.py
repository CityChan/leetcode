class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[float('inf')]*3 for _ in range(n)]
        dp[0] = costs[0] 
        for i in range(1, n):
            dp[i][0] =  min(dp[i-1][1]+costs[i][0], dp[i-1][2]+costs[i][0])
            dp[i][1] =  min(dp[i-1][0]+costs[i][1], dp[i-1][2]+costs[i][1])
            dp[i][2] =  min(dp[i-1][0]+costs[i][2], dp[i-1][1]+costs[i][2])
        return min(dp[n-1])
        
