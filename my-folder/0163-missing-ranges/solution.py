class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if len(nums) == 0:
            return [[lower, upper]]
        ans = []
        if nums[0] > lower:
            ans.append([lower, nums[0]-1])

        left, right = 0, 0
        for i in range(len(nums)-1):
            if lower <= nums[i] <= nums[i+1] <= upper:
                left = nums[i] + 1
                right = nums[i+1] - 1
                if left <= right:
                    ans.append([left, right])
            elif lower <= nums[i] <= upper < nums[i+1]:
                left = nums[i] + 1
                right = upper - 1
                if left <= right:
                    ans.append([left, right])
                break

            elif  nums[i] < lower <= upper < nums[i+1]:
                left = lower + 1
                right = nums[i+1] - 1
                break

            elif  nums[i] < lower <= nums[i+1] < upper:
                left = lower + 1
                right = nums[i+1] - 1
                if left <= right:
                    ans.append([left, right])
        if nums[-1] < upper:
            ans.append([nums[-1]+1, upper])
        return ans
