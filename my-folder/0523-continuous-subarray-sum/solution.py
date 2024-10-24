class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {0 : -1}
        s = 0
        for i in range(len(nums)):
            s = (s+nums[i])%k
            if s not in hmap:
                hmap[s] = i
            if i - hmap[s] > 1:
                return True
        return False
                 


