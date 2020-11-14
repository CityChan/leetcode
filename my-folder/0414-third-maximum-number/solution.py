class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max = float('-inf')
        secMax = float('-inf')
        thirdMax = float('-inf')
        
        for num in nums:
            if num == max or num == secMax or num == thirdMax:
                continue
            if num > max:
                thirdMax = secMax
                secMax = max
                max = num
            elif num > secMax:
                thirdMax = secMax
                secMax = num
            elif num > thirdMax:
                thirdMax = num
                
        return thirdMax if thirdMax != float('-inf') else max
