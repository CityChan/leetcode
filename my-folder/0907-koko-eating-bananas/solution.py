class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        Max = max(piles)
        left, right = 1, Max
        while left < right:
            mid = left + (right - left) // 2
            if self.TimeNeed(piles, mid) <= h:
                right = mid 
            else:
                left = mid + 1
        
        return left

        
    def TimeNeed(self, piles, k):
        h = 0
        for i in range(len(piles)):
            h += piles[i] // k
            if piles[i] % k > 0:
                h += 1
        return h


