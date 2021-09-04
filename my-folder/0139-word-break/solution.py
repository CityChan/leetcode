class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[True]
        for i in range(1, len(s)+1):
            if any([dp[j] and s[j:i] in wordDict for j in range(0, i)]):
                dp+=[True]
            else:
                dp+=[False]
                
        return dp[-1]
        
