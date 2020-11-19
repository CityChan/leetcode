class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] * n
        left = 0
        right = n - 1
        while left < right:
            ans[left] = - right
            ans[right] = right
            left = left+1
            right = right-1

        return ans
