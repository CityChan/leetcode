class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            print(left, mid, right, self.Cnt(nums, mid), mid)
            if self.Cnt(nums, mid) <= mid:
                left = mid + 1
            if self.Cnt(nums, mid) > mid:
                right = mid 
        return left
        
    def Cnt(self, nums, k):
        cnt = 0
        for num in nums:
            if num <= k:
                cnt += 1
        return cnt
