class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0]+sorted(horizontalCuts)+[h]
        verticalCuts = [0]+sorted(verticalCuts)+[w]
        return (max([j-i for i, j in zip(horizontalCuts[:-1], horizontalCuts[1:])])*max([j-i for i, j in zip(verticalCuts[:-1], verticalCuts[1:])]))%(10**9 + 7)
            
            
            
        
