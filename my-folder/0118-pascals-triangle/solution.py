class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        m=[]
        for i in range(1,numRows+1):
            c=1
            t=[]
            for j in range(1,i+1):
                t.append(c)
                c=int(c*(i-j)/j)
            m.append(t)
        return m
