class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount<0:
            return 0
        res = [amount+1]*amount
        def bfs(amt):
            if amt<0:
                return -1
            elif amt==0:
                return 0
            else:
                if res[amt-1]!=amount+1:
                    return res[amt-1]
                else:
                    for c in coins:
                        temp = bfs(amt-c)
                        if temp>=0 and temp<res[amt-1]:
                            res[amt-1] = temp+1
            res[amt-1] = res[amt-1] if res[amt-1]<amount+1 else -1
            return res[amt-1]
        return bfs(amount)

