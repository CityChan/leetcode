class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict = {}
        res = 0
        for num in nums:
            if num in dict:
                res += dict[num]
                dict[num] += 1
            else:
                dict[num] = 1
                
        return res
