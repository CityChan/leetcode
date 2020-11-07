class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        firstIndex = {}
        count = {}
        degree = 0
        res = 0
        
        for i, number in enumerate(nums):
            firstIndex.setdefault(number, i)
            count[number] = count.get(number, 0) + 1
            if count[number] > degree:
                degree = count[number]
                res = i - firstIndex[number] + 1
            elif count[number] == degree:
                res = min(res, i - firstIndex[number] + 1)
                
        return res
                
