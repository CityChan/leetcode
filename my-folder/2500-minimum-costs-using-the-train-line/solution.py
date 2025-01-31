class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        n = len(regular)
        f = [0]*(n+1)
        g = [float('inf')]*(n+1)
        cost = [0]*n
        for i, (a,b) in enumerate(zip(regular, express), 1):
            f[i] = min(f[i-1] + a, g[i-1] + a)
            g[i] = min(g[i-1] + b, f[i-1] + b + expressCost)
            cost[i - 1] = min(f[i], g[i])
        return cost
