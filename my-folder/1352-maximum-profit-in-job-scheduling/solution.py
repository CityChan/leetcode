class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[0])
        dp = [[10**9, 0]]
        for s, e, p in jobs[::-1]:
            i = bisect.bisect(dp, [e])
            if dp[i][1] + p > dp[0][1]:
                dp = [([s, dp[i][1] + p])]+dp
        return dp[0][1]
        
