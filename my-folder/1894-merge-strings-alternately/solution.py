class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i = 0
        while i< min(len(word1), len(word2)):
            res+=word1[i]
            res+=word2[i]
            i+=1
        if i<=len(word1)-1:
            res+=word1[i:len(word1)]
        else:
            res+=word2[i:len(word2)]
        return res
