class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == -2**31:
            return self.myPow(1/x, -(n+1))/x
        if n < 0:
            return self.myPow(1/x, -n)
        if n%2 == 1:
            return x*self.myPow(x, n - 1)
        else:
            sub = self.myPow(x, n // 2)
            return sub*sub
