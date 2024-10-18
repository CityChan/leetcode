class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        res = ''
        for i in range(n):
            if not (s[i].islower() or s[i].isdigit()):
                if s[i].isupper():
                    res += s[i].lower()
                else:
                    continue
            else:
                res += s[i]
        left, right = 0, len(res)-1
        while left <= right:
            if res[left] != res[right]:
                return False
            else:
                left +=1
                right -=1
        return True
