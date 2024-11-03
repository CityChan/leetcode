class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        path = []
        self.backtrack(nums, 0, path)
        return self.res

    def backtrack(self, nums, start, path):
        self.res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, i+1, path)
            path.pop()
    

