class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used = [False]*len(nums)
        now_res = []
        def traverse(now_res):
            if len(now_res)==len(nums):
                res.append(now_res)
            else:
                for i in range(len(nums)):
                    if used[i]!=True:
                        used[i]=True
                        traverse(now_res+[nums[i]])
                        used[i]=False
                
        traverse([])
        return res

        
