class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = Counter({0:1})
        ans, acc = 0, 0
        for num in nums:
            acc += num
            ans += hashmap[acc - k]
            hashmap[acc] += 1
        return ans
