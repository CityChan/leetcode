class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid]>=target:
                end = mid-1
            else:
                start = mid+1
        if start == len(nums) or nums[start]!=target:
            return [-1, -1]
        left = start
        
        end = len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
        return [left, end]
        
        
        
