class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        queue = []
        for i, n in enumerate(nums):
            while queue and nums[queue[-1]]<=n:
                queue.pop()
                        
            queue.append(i)
            if queue[0]==i-k:
                queue.pop(0)
                
            if i>=k-1:
                res.append(nums[queue[0]]) 
        return res
        
