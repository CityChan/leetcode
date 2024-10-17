class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need = 0
        ans = 0
        for c in s:
            if c == '(':
                need += 1
            if c == ')':
                if need > 0:
                    need -= 1
                else:
                    ans += 1
        return ans + need
                    
