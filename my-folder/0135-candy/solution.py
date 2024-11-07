class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for j in range(n-2,-1, -1):
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1] + 1
        return sum(max(a, b) for a, b in zip(left, right)) 
