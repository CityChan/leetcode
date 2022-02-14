class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0
        farthest = 0
        now = 0
        if len(nums)==1:
            return 0
        for i, n in enumerate(nums):
            farthest = max(farthest, i+n)
            if i==now:
                step+=1
                now = farthest
                if len(nums)-1<=farthest:
                    return step
                    
                    
        
