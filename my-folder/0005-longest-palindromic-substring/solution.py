class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(s, i, j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return i+1, j-1
        
        max_len = 0
        max_str = ""
        for n in range(len(s)):
            i, j = helper(s, n, n)
            if j-i+1>max_len:
                max_len = j-i+1
                max_str = s[i:j+1]
            if (n+1)<len(s) and s[n]==s[n+1]:
                i, j = helper(s, n, n+1)
                if j-i+1>max_len:
                    max_len = j-i+1
                    max_str = s[i:j+1]
        return max_str
                
                
            
        
