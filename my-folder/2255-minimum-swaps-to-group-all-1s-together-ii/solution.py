class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n_ones = sum(nums)
        n = len(nums)
        
        if n_ones == 0:
            return 0
        
        cur = 0
        for i in range(n_ones):
            cur += 1 - nums[i]
            
        ans = cur
        for i in range(1, n):
            if nums[i-1] == 0:
                cur -= 1
            if nums[(i+n_ones-1)%n] == 0:
                cur += 1
            ans = min(ans, cur)
        return ans
