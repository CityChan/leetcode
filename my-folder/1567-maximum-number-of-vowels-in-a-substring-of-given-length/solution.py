class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c = 0
        for i in range(k):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                c+=1
        max_v = c
        for i in range(len(s)-k):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                c-=1
            if s[k+i] in ['a', 'e', 'i', 'o', 'u']:
                c+=1
            max_v = max(max_v, c)
        return max_v
