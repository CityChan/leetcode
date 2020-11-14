class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        leftSum = A[0]
        rightSum = A[-1]
        average = sum(A) // 3

        l, r = 1, len(A) - 2
        while l < r:
            if l < r and leftSum != average:
                leftSum += A[l]
                l += 1
            if l < r and rightSum != average:
                rightSum += A[r]
                r -= 1
            if leftSum == average == rightSum and sum(A) % 3 == 0:
                return True
            if l == r:
                break
        return False
