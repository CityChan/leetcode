class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = Counter({0:1})
        ans, acc = 0, 0
        for num in nums:
            acc += num
            ans += count[acc - k]
            count[acc] += 1
        return ans
