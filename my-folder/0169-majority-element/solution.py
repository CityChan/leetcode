class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for num in set(nums):
            if counter.get(num) > len(nums) // 2:
                return num
