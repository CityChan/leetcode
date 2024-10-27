class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if s[0] == '0':
            return 0
        if n <= 1:
            return 1

        dp = [0 for _ in range(n)]
        dp[0] = 1
        two_digit = 10*int(s[0]) + int(s[1])
        if s[1] == '0' and two_digit > 26:
            dp[1] = 0
        elif s[1] == '0' and two_digit <= 26:
            dp[1] = 1
        elif s[1] != '0' and two_digit <= 26:
            dp[1] = 2
        else:
            dp[1] = 1
        
        for i in range(2, n):
            prev = int(s[i-1])
            cur = int(s[i])
            print(prev,cur)
            two_digit = int(prev)*10 + int(cur)
            if  cur == 0 and prev != 0 and two_digit > 26:
                dp[i] = 0
            elif cur == 0 and prev != 0 and two_digit <= 26:
                dp[i] = dp[i-2]
            elif cur != 0 and prev != 0 and two_digit > 26:
                dp[i] = dp[i-1]
            elif cur != 0 and prev != 0 and two_digit <= 26:
                dp[i] = dp[i-2] + dp[i-1]
            elif cur == 0 and prev != 0 and two_digit <= 26:
                dp[i] = dp[i-2]
            elif prev == 0 and cur == 0:
                dp[i] = 0
            elif prev == 0 and cur != 0:
                dp[i] = dp[i-1]
        print(dp)
        return dp[-1]
