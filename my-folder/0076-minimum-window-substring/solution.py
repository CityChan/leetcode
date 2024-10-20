class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        window = len(s)
        ans = ""
        needs = [0]*256
        for v in t:
            idx = ord(v)  - ord('A') 
            needs[idx] += 1
        left, right = 0, 0
        while right < len(s):
            if s[right] in t:
                needs[ord(s[right]) - ord('A')] -= 1
                while max(needs) <= 0:
                    if right - left + 1 <= window:
                        window = right - left + 1
                        ans = s[left:right+1]
                    if s[left] in t:
                        needs[ord(s[left]) - ord('A')] += 1
                        print(needs[ord('b') - ord('A')])
                    left += 1
            right += 1
        return ans if ans != "" else ""


