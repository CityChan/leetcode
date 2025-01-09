class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        q = defaultdict(list)
        s_min, e_max = inf, 0
        for s,e in events:
            q[s].append(e)
            s_min = min(s, s_min)
            e_max = max(e_max, e)

        h = []
        ans = 0
        for t in range(s_min, e_max+1):
            while h and h[0] < t:
                heappop(h)
            for e in q[t]:
                heappush(h,e)
            if h:
                ans += 1
                heappop(h)
        return ans

