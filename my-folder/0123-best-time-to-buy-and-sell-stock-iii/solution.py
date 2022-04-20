class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        k = 2
        states = [0] + [-float('inf') for i in range(2*k)]
        states[1] = -prices[0]
 
        for i in range(1, len(prices)):
            for j in range(k):
                states[2*j+1] = max(states[2*j+1], states[2*j]-prices[i])
                states[2*j+2] =   max(states[2*j+2], states[2*j+1]+prices[i])
        
        return max(0, states[-1])

