class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        three_max = heapq.nlargest(3, nums)
        two_min = heapq.nsmallest(2, nums)
        return max(three_max[0] * three_max[1] * three_max[2], three_max[0] * two_min[0] * two_min[1]);
