class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        
        res = [[0]*(n+1) for _ in range(m+1)]
        for j in range(1, n+1):
            res[0][j]=j
        for i in range(1, m+1):
            res[i][0]=i
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1]==word2[j-1]:
                    res[i][j]=res[i-1][j-1]
                else:
                    res[i][j]=min(res[i-1][j], res[i][j-1], res[i-1][j-1])+1
        return res[m][n]
        
