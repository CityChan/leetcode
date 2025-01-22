class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            need = target - nums[i]
            if need in hashmap:
                return [hashmap[need], i]
            hashmap[nums[i]] = i
        return []


