class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            i=1
            j=2
            for k in range(3, n+1):
                j, i = j+i, j
            return j
        
