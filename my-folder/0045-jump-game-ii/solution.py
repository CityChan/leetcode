class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        res = [[0]]
        while len(nums)-1 not in res[-1]:
            temp_res = set()
            for i in res[-1]:
                for j in range(1, nums[i]+1):
                    temp_res.add(i+j)
            res+=[temp_res]
            count+=1
        return count
                    
            
