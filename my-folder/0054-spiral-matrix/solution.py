class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        u = 0
        d = len(matrix)-1
        l = 0
        r = len(matrix[0])-1
        res = []
        while len(res)<len(matrix)*len(matrix[0]):
            if u<=d:
                for i in range(l, r+1):
                    res.append(matrix[u][i])
                u+=1
            if l<=r:
                for i in range(u, d+1):
                    res.append(matrix[i][r])
                r-=1
            if u<=d:
                for i in reversed(range(l, r+1)):
                    res.append(matrix[d][i])
                d-=1
            if l<=r:
                for i in reversed(range(u, d+1)):
                    res.append(matrix[i][l])
                l+=1
            # print(u, d, l, r)
        return res
                
            
