class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        count=0
        now_pos = 0
        far_range = 0
        for i in range(len(nums)):
            far_range = max(far_range, nums[i]+i)
            if i==now_pos:
                count+=1
                now_pos = far_range
                if now_pos>=len(nums)-1:
                    return count
            
