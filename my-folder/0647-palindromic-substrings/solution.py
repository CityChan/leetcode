class Solution:
    def countSubstrings(self, s: str) -> int:
        ans, m = 0, len(s)
        for k in range(2*m):
            l, r = k//2, (k+1)//2
            while l >= 0 and r < m and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans
