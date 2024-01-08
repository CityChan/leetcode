class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        max_1 = 0
        c = 0
        while right<len(nums):
            while right<len(nums) and (nums[right]==1 or (nums[right]==0 and c<k)):
                if nums[right]==0:
                    c+=1
                right+=1
            max_1 = max(max_1, right-left)
            while left<len(nums) and nums[left]!=0:
                left+=1
            left+=1
            c-=1
        return max_1
                    
        
