class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        
        max_len = 0
        res_list = [0]
        for i in range(len(nums)):
            if i==0 or nums[i]==nums[i-1]+1:
                max_len = max(max_len, res_list[-1]+1)
                res_list.append(res_list[-1]+1)
            else:
                res_list.append(1)
        return max_len
            
        
