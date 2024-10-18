class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stk = []
        n = len(heights)
        stk.append(n-1)
        for i in range(n-2, -1, -1):
            if heights[i] > heights[stk[-1]]:
                stk.append(i)
        stk.sort()
        return stk
                
            
