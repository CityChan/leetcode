class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
#         low+1 == high 
        while low < high:  
            mid = (low + high) // 2
            # if nums[mid] == target:
            #     return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low
    
#     1, 3, 5, 6
#     l  m     h  t=7
#             l/m l
#        
#        
