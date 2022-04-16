class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return list(range(1, n//2+1)) + list(range(-1, -(n//2)-1, -1)) + ([0] if n%2==1 else [])
