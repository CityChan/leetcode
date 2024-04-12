class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        prev_max_skip = 0
        for i in nums:
            # final_max = max(prev_max_skip+nums[i], prev_max)
            prev_max, prev_max_skip = max(prev_max_skip+i, prev_max), prev_max
        return max(prev_max_skip, prev_max)
        
