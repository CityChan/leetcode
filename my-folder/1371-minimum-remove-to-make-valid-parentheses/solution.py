class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        left, right = 0, s.count(')')
        for c in s:
            if c == ')':
                print(1)
                if left > 0:
                    ans += c
                    left -= 1
                else:
                    right -= 1
            elif c == '(':
                if right > 0:
                    ans += c
                    right -= 1
                    left += 1

            else:
                ans += c
        return ans
