class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0] 
        left, right = 0, n
        while left < right:
            mid = left + (right - left )//2
            if nums[0] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
