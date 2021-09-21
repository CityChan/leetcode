class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(s, i, j):
            while i>=0 and j<=len(s)-1:
                if s[i]==s[j]:
                    i-=1
                    j+=1
                else:
                    break
            return s[i+1:j]
        res=""
        for i in range(len(s)):
            res1=helper(s, i, i)
            if len(res1)>len(res):
                res = res1
            if i<len(s)-1 and s[i]==s[i+1]:
                res1=helper(s, i, i+1)
                if len(res1)>len(res):
                    res = res1
        return res
            
                
            
        
