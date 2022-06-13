class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        now = nums[0]
        for i in range(1, len(nums)):
            now, pre = max(pre+nums[i], now), now
        return max(pre, now)
        
