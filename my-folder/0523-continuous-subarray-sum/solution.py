class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {0 : -1}
        s = 0
        for i,x in enumerate(nums):
            s = (s + x)%k
            if s not in hmap:
                hmap[s] = i
            elif i - hmap[s] > 1:
                return True
        return False


