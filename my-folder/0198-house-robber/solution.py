class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2,n):
            print(dp)
            dp[i] = max(dp[i-2] + nums[i], dp[i-1] - nums[i-1] + max(nums[i-1], nums[i]))
            
        print(dp)
        return dp[n-1]

