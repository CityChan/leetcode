class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        max_h = 0
        res = []
        for i in range(len(heights)):
            if heights[len(heights)-1-i]>max_h:
                res+=[len(heights)-1-i]
                max_h = heights[len(heights)-1-i]
        return res[::-1]
                
        
