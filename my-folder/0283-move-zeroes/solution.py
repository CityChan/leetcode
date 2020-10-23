class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        while slow < len(nums) and nums[slow] != 0:
            slow += 1

        fast = slow
        # nums[slow]:0
        while fast < len(nums):
            if nums[fast] != 0:
                tmp = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = tmp

            if nums[slow] != 0:
                slow += 1
            fast += 1
