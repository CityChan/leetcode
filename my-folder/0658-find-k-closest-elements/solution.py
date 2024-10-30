class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        p = self.left_bound(arr, x)
        left = p - 1
        right = p
        res = collections.deque()
        while right - left - 1 < k:
            if left == -1:
                res.append(arr[right])
                right += 1
            elif right == len(arr):
                res.appendleft(arr[left])
                left -= 1
            elif x - arr[left] > arr[right] - x:
                res.append(arr[right])
                right += 1
            else:
                res.appendleft(arr[left])
                left -= 1
        return list(res)

    def left_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

