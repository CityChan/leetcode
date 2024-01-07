class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_cumprod = [1]
        for n in nums[:-1]:
            left_cumprod.append(left_cumprod[-1]*n)
        right_cumprod = [1]
        for n in nums[len(nums)-1:0:-1]:
            right_cumprod.append(right_cumprod[-1]*n)
        return [left_cumprod[i]*right_cumprod[len(nums)-1-i] for i in range(len(nums))]
            
            
        
