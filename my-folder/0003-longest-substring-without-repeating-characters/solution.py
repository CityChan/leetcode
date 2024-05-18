class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        char_set = set()
        while right<len(s):
            if s[right] not in char_set:
                char_set.add(s[right])
                if right==len(s)-1:
                    max_len = max(max_len, right-left+1)
            else:
                max_len = max(max_len, right-left)
                while s[left]!=s[right]:
                    print(char_set)
                    char_set.remove(s[left])
                    left+=1
                left+=1
            right+=1
        return max(max_len, right-left)
        
