class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        backup = k
        max_window = 0
        left, right = 0, 0
        while right < len(nums):
            print(left, right, backup)
            if nums[right] == 1:
                right += 1
            else:
                if backup > 0:
                    backup -= 1
                    right += 1
                else:
                    max_window = max(max_window, right - left)
                    if nums[left] == 0:
                            backup +=1
                    left += 1
        max_window = max(max_window, right - left)
        return max_window
