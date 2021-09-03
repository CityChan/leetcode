class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pre = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[pre]=nums[i]
                pre+=1
        # for i in range(pre, len(nums)):
        #     nums[i]=0
        return pre
            
                
        
