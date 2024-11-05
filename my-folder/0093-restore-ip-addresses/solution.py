class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.dfs(s, 0, [])
        return self.res
    def dfs(self, s, start, ans):
        m = len(s)
        if start >= m and len(ans) == 4:
            self.res.append(".".join(ans))
            return 
        if start >= m or len(ans) >= 4:
            return
        for end in range(start, min(start+3, m)):
            if s[start] == "0" and start != end:
                continue
            if 0 <= int(s[start:end+1]) <= 255:
                ans.append(s[start:end+1])
                self.dfs(s, end + 1, ans)
                ans.pop()
        return
