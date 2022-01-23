class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        now_subsum=nums[0]
        max_subsum=nums[0]
        for i in nums[1:]:
            now_subsum = max(now_subsum+i, i)
            max_subsum = max(now_subsum, max_subsum)
        return max_subsum
            
        
