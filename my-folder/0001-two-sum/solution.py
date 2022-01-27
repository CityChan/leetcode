class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        save_list = [None]*len(nums)
        for i, n in enumerate(nums):
            save_list[i] = target - n
        for i, n in enumerate(nums):
            try:
                find_idx = save_list.index(n)
                if i != find_idx:
                    return [i, find_idx]
            except:
                continue
        
        # save_dict = {}
        # for i, n in enumerate(nums):
        #     save_dict[target-n] = i
        # for i, n in enumerate(nums):
        #     if n in save_dict and save_dict[n]!=i:
        #         return [i, save_dict[n]]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         save_dict = {}
#         for i, n in enumerate(nums):
#             save_dict[target-n]=i
        
#         for i, n in enumerate(nums):
#             if n in save_dict:
#                 if i!=save_dict[n]:
#                     return [i, save_dict[n]]
            
        
        
