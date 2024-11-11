class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                need += 1
            if s[i] == ')':
                if need > 0:
                    need -= 1
                else:
                    res += 1
        return res + need




