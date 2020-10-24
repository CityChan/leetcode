class Solution:
    def missingNumber(self, nums: List[int]) -> int:
         sortedNums = sorted(nums)
        
         for i in range(len(nums)):
            if i != sortedNums[i]:
                return i
        
         return len(nums)
