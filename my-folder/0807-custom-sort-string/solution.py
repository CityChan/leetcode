class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hashmap = {}
        for i, c in enumerate(order):
            hashmap[c] = i
        
        s = list(s)
        in_order = []
        sub_s = []
        for i,c in enumerate(s):
            if c in hashmap:
                in_order.append(i)
                sub_s.append(c)
        sub_s.sort(key = lambda x: hashmap[x])
        ans = []
        for i,c in enumerate(s):
            if c in hashmap:
                ans.append(sub_s.pop(0))
            else:
                ans.append(c)
        return "".join(ans)


