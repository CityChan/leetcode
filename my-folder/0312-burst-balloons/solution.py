class Solution:
    def maxCoins(self, nums: List[int]) -> int:
    # def maxCoins(self, iNums):
    #     nums = [1] + [i for i in iNums if i > 0] + [1]
    #     n = len(nums)
    #     dp = [[0]*n for _ in xrange(n)]

    #     for k in xrange(2, n):
    #         for left in xrange(0, n - k):
    #             right = left + k
    #             for i in xrange(left + 1,right):
    #                 dp[left][right] = max(dp[left][right],
    #                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    #     return dp[0][n - 1]
    
        nums = [1]+nums+[1]
        dp = [[0]*len(nums) for _ in range(len(nums))]
        for k in range(2, len(nums)):
            for left in range(0, len(nums)-k):
                right = left+k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right], nums[left]*nums[i]*nums[right]+dp[left][i]+dp[i][right])
        
        return dp[0][len(nums)-1]
        
        
