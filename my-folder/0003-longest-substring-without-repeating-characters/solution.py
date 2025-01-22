class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        left, right = 0, 0
        Set = set()
        while right < n:
            entry = s[right]
            while entry in Set:
                Set.remove(s[left])
                left += 1
            Set.add(entry)
            ans = max(ans, len(Set))
            right += 1
        return ans
                
