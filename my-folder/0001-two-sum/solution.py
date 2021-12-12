class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        save_dict = {}
        for i, n in enumerate(nums):
            save_dict[target-n]=i
        
        for i, n in enumerate(nums):
            if n in save_dict:
                if i!=save_dict[n]:
                    return [i, save_dict[n]]
            
        
        
