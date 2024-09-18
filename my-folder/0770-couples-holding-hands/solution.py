class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        n = len(row) // 2
        p = list(range(n))
        for i in range(0, 2*n, 2):
            a = row[i]//2
            b = row[i+1] // 2
            p[find(a)] = find(b)
        return n - sum(i == find(i) for i in range(n))
