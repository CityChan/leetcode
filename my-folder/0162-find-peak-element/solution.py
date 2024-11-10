import heapq
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        if len(nums) == 1:
            return 0
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[mid+1]:
                left = mid + 1
            elif nums[mid] > nums[mid+1]:
                right = mid
        return left
