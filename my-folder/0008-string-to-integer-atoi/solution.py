class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        sign = 1
        res = 0
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1
        while i < n and '0' <= s[i] <= '9':
            res = res*10 + ord(s[i]) - ord('0')
            if sign == 1 and res > 2**31 - 1:
                return 2**31 - 1
            if sign == -1 and res > 2**31 - 1:
                return -2**31
            i += 1
        return int(res)*sign
