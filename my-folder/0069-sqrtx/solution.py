class Solution:
    def mySqrt(self, x: int) -> int:
        cur = 1
        while cur*cur <= x:
            cur += 1

        return cur-1 
            
