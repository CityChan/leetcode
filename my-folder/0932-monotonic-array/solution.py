class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return all(x <= y for x, y in zip(A, A[1:])) or all(x >= y for x, y in zip(A, A[1:]))

