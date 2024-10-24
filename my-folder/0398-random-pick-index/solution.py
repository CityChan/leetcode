class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.indices = {}
        for index, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(index)

    def pick(self, target: int) -> int:
        return choice(self.indices[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
