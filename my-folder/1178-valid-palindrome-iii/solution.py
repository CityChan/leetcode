class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        s_r = s[::-1]
        res = [[0]*(len(s)+1) for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(s)+1):
                if s[i-1]==s_r[j-1]:
                    res[i][j]=res[i-1][j-1]+1
                else:
                    res[i][j]=max(res[i-1][j], res[i][j-1])
        return res[len(s)][len(s)]>=len(s)-k
        
