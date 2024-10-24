class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        memo = []
        for i, num in enumerate(nums):
            for j, n in enumerate(num):
                memo.append([i+j, j, n])
        memo.sort(key = lambda x: (x[0], x[1]))
        ans = []
        for v in memo:
            ans.append(v[2])
        return ans
