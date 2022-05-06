class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [1]*len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    res[i] = max(res[j]+1, res[i])
        return max(res)
                
