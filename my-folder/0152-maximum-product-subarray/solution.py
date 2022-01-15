class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curMax, curMin = 1, 1
        finalMax = -10
        for n in nums:
            curMax, curMin = max(n, curMax*n, curMin*n), min(n, curMax*n, curMin*n)
            finalMax = max(curMax, finalMax)
        return finalMax
        
