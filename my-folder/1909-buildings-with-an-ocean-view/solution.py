class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        res = []
        highest = 0
        for i, h in enumerate(heights[::-1]):
            if h>highest:
                res.append(i)
            highest = max(highest, h)
        return [len(heights)-1-i for i in res[::-1]]
        
