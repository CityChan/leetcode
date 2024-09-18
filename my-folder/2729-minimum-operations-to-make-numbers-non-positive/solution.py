class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        def check(t):
            cnt = 0
            for v in nums:
                if v > t*y:
                    cnt += ceil((v - t*y)/(x - y))
            return cnt <= t
        
        left, right = 0, max(nums)
        while left < right:
            mid = left + (right - left)//2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
