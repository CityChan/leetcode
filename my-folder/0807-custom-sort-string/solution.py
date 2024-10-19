class Solution:
    def customSortString(self, order: str, s: str) -> str:
        idx_order = []
        ans_order = ""
        for i, v in enumerate(s):
            if v in order:
                idx_order.append(i)
                ans_order += v
        counter = Counter(ans_order)
        ans_order = ""
        for v in order:
            if v in s:
                for i in range(counter[v]):
                    ans_order += v
        ans = ''
        cur = 0
        for i in range(len(s)):
            if i in idx_order:
                ans+= ans_order[cur]
                cur+= 1
            else:
                ans+= s[i]
        return ans
