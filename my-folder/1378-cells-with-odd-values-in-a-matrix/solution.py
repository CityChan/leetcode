class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        x = [0] * n
        y = [0] * m

        for r, c in indices:
            x[r] += 1
            y[c] += 1

        return sum([ (r+c) % 2 for c in y for r in x])
