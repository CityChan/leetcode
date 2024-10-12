from sortedcontainers import SortedList

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        m = max([q[1] for q in queries])+1
        t = [0]*m
        
        def update(i, val):
            while i < m:
                t[i] = max(t[i],val)
                i += i & (-i)
        
        def pre_max(i):
            ans = 0
            while i:
                ans = max(ans, t[i])
                i -= i&(-i)
            return ans
        
        pos = [0] + sorted([q[1] for q in queries if q[0] == 1])
        for p, q in pairwise(pos):
            update(q, q - p)
        sl = SortedList(pos)
        sl.add(m) 
        
        ans = []
        for q in reversed(queries):
            x = q[1]
            i = sl.bisect_left(x)
            pre = sl[i - 1] 
            if q[0] == 1:
                sl.discard(x)
                nxt = sl[i]  
                update(nxt, nxt - pre)  
            else:
                max_gap = max(pre_max(pre), x - pre)
                ans.append(max_gap >= q[2])
        return ans[::-1]

