class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        if nums[0] >= 0:
            dp[0] = True
        for i in range(1, n):
            cur = i-1
            while cur >= 0 and nums[cur] <= i-1 - cur:
                cur -= 1
            if cur >= 0:
                dp[i] = dp[cur]
        return dp[n-1]
