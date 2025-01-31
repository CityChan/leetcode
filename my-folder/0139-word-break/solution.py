class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [True] + [False for _ in range(n)]
        for i in range(1, n+1):
            dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
        return dp[n]
