class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        delta = float('inf')
        for i in range(len(nums)-2):
            sum_ = nums[i] + self.twoSumClosest(nums, i + 1, target - nums[i])
            if abs(delta) > abs(target - sum_):
                delta = target - sum_
        return target - delta

    def twoSumClosest(self, nums, start,target):
        lo, hi = start, len(nums) - 1
        delta = float('inf')
        while lo < hi:
            sum_ = nums[lo] + nums[hi]
            if abs(delta) > abs(target - sum_):
                delta = target - sum_
            if sum_ < target:
                lo +=1
            else:
                hi -= 1
        return target - delta
        
