class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        unique = set(s)
        maxUnique = len(unique)
        res = 0
        for currUnique in range(1,maxUnique+1):
            countMap = [0]*26
            windowleft, windowright = 0, 0
            unique = 0
            countAtLeastK = 0
            idx = 0
            while  windowright < len(s):
                if unique <= currUnique:
                    idx = ord(s[windowright]) - ord('a')
                    if countMap[idx] == 0:
                        unique += 1
                    countMap[idx] += 1
                    if countMap[idx] == k:
                        countAtLeastK += 1
                    windowright += 1
                else:
                    idx = ord(s[windowleft]) - ord('a')
                    if countMap[idx] == k:
                        countAtLeastK -= 1
                    countMap[idx] -= 1
                    if countMap[idx] == 0:
                        unique -= 1
                    windowleft += 1
                if unique == currUnique and unique == countAtLeastK:
                    res = max(windowright - windowleft, res)
        return res
                    
                
        
