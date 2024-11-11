class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stk = []
        for i,h in enumerate(heights):
            while stk and heights[stk[-1]] <= h:
                stk.pop()
            stk.append(i)
        return stk
                
            
