class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        ans = 0
        stk = set()
        for j,c in enumerate(s):
            while s[j] in stk:
                stk.remove(s[i])
                i += 1
            stk.add(c)
            ans = max(ans, j - i + 1)
        return ans
            
            

            
        
