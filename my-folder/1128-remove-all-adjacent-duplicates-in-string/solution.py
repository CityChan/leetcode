class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        ans = []
        ans.append(s[0])
        for i in range(1, n):
            if ans and s[i] == ans[-1]:
                ans.pop()
            else:
                ans.append(s[i])
        return "".join(ans)

