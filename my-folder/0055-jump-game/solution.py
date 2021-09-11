class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        end = len(nums)-1
        i = len(nums)-2
        while i>=0:
            if nums[i]+i>=end:
                end = i
            i-=1
        if end == 0:
            return True
        else:
            return False
        
