class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1
