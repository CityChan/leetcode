class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        i1 = 1
        i2 = 2
        for i in range(3, n+1):
            i1, i2 = i2, i1+i2
        return i2
        
