class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minCost = prices[0]
        maxProfit = 0
        for p in prices[1:]:
            if p>=minCost:
                maxProfit = max(maxProfit, p-minCost)
            else:
                minCost = min(minCost, p)
        return maxProfit
                
        
