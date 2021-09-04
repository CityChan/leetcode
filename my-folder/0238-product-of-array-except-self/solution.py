class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum = 1
        left_cum = [1]
        for i in range(1, len(nums)):
            cum *= nums[i-1]
            left_cum.append(cum)
        
        cum = 1
        for i in range(len(nums)-1, -1, -1):
            left_cum[i]*=cum
            cum *= nums[i]
        return left_cum
        
