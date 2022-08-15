class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used = [False]*len(nums)
        def traverse(now_res, step):
            if step==len(nums):
                res.append(now_res)
            else:
                for i in range(len(nums)):
                    if used[i]!=True:
                        used[i]=True
                        # traverse(now_res, step+1)
                        traverse(now_res+[nums[i]], step+1)
                        used[i]=False
                
        traverse([], 0)
        return res

        
