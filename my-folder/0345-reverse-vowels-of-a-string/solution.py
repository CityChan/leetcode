class Solution:
    def reverseVowels(self, s: str) -> str:
        idx_list = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u']+[x.upper() for x in ['a', 'e', 'i', 'o', 'u']]:
                idx_list.append(i)
        print(idx_list)
        for i in range(len(idx_list)//2):
            s[idx_list[i]], s[idx_list[len(idx_list)-i-1]] = s[idx_list[len(idx_list)-i-1]], s[idx_list[i]]
            
        return "".join(s)
        
