class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_size = len(nums)+1
        start = 0
        end = 0
        s = 0
        while end<len(nums):
            s+=nums[end]
            if s>=target:
                while s-nums[start]>=target:
                    s -= nums[start]
                    start+=1
                min_size = min(min_size, end-start+1)
            end+=1
        return 0 if min_size==len(nums)+1 else min_size
            
