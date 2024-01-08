class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 0
        l = 0
        u = 0
        r = n-1
        d = n-1
        res = [[0 for _ in range(n)] for _ in range(n)]
        while count<n*n:
            if u<=d:
                for i in range(l, r+1):
                    count+=1
                    res[u][i] = count
                u+=1
            if l<=r:
                for i in range(u, d+1):
                    count+=1
                    res[i][r] = count
                r-=1
            if d>=u:
                for i in range(r, l-1, -1):
                    count+=1
                    res[d][i] = count
                d-=1
            if r>=l:
                for i in range(d, u-1, -1):
                    count+=1
                    res[i][l] = count
                l+=1
            
        return res
