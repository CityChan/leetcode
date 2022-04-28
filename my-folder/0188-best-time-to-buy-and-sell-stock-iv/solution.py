class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k==0:
            return 0
        buy = [-2000]*k
        sell = [0]*k
     
        for i in range(len(prices)):
            for j in range(k):
                if j==0:
                    buy[j] = max(buy[j], -prices[i])
                else:
                    buy[j] = max(buy[j], sell[j-1]-prices[i])
                sell[j] = max(sell[j], buy[j]+prices[i])
        return sell[-1]
        
