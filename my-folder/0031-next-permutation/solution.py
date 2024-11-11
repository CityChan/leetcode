class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = -1
        j = -1
        for k in range(n-2, -1, -1):
            if nums[k] < nums[k + 1]:
                i = k
                break
        if i >= 0:
            for k in range(n-1, -1, -1):
                if nums[k] > nums[i]:
                    j = k
                    break

        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        nums[i+1:] = nums[i+1:][::-1]
        return nums
