class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def ifPalindrome(l, r):
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    l-=1
                    r+=1
                else:
                    break
            return l+1, r-1
        
        max_len = 0
        max_l = 0
        max_r = 0
        
        for i in range(len(s)):
            l, r = ifPalindrome(i, i)
            if r-l+1>max_len:
                max_l = l
                max_r = r
                max_len = r-l+1

        for i in range(len(s)-1):
            l, r = ifPalindrome(i, i+1)
            if r-l+1>max_len:
                max_l = l
                max_r = r
                max_len = r-l+1
                
        return s[max_l:max_r+1]
                
            
            
        
