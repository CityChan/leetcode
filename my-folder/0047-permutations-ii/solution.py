class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        used = [False]*len(nums)
        now_res = []
        res = []
        def traverse(now_res):
            if len(now_res)==len(nums):
                res.append(now_res)
            else:
                for i in range(len(nums)):
                    if i>0 and nums[i]==nums[i-1] and used[i-1]!=True:
                        continue
                    if used[i]==False:
                        used[i]=True
                        traverse(now_res+[nums[i]])
                        used[i]=False
        traverse([])
        return res
