class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minCost = prices[0]
        maxProfit = 0
        for p in prices[1:]:
            maxProfit = max(maxProfit, p-minCost)
            minCost = min(minCost, p)
        return maxProfit
                
        
