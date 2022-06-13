class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def rob_sub(nums):
            pre = 0
            now = nums[0]
            for i in range(1, len(nums)):
                now, pre = max(pre+nums[i], now), now
            return max(now, pre)
                
        return nums[0] if len(nums)==1 else max(rob_sub(nums[:-1]), rob_sub(nums[1:]))
