class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<len(nums) and nums[j]==nums[j-1]:
                        j+=1
                    while k>i and nums[k]==nums[k+1]:
                        k-=1
        return res
                    

