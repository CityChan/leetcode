class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
#         subprices = [prices[i+1]-prices[i] for i in range(len(prices)-1)]
#         i=0
#         while i<len(subprices) and subprices[i]<0:
#             i+=1
            
#         s = 0
#         s_max = 0
#         for j in range(i, len(subprices)):
#             s+=subprices[j]
#             s_max = max(s, s_max)
#             if s<0:
#                 s=0
#         return s_max
                
        if len(prices)==1:
            return 0
        i, j = 0, 1
        while j<len(prices) and prices[j]-prices[i]<=0:
            i+=1
            j+=1
        if j==len(prices):
            return 0
        
        s_max = 0
        
        while j<len(prices):
            s_max = max(s_max, prices[j]-prices[i])
            if prices[j]-prices[i]<=0:
                i=j
                j=i+1
            else:
                j+=1
        return s_max
        
        
        
