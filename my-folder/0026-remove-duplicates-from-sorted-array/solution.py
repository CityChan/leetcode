class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        index = 0
        for i in range(1, len(nums)):
            if nums[index] < nums[i]:
                index += 1
                nums[index] = nums[i]
        nums = nums[: index+1]        
        
        return len(nums)
        
