class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last_num = 0
        k_index = 0

        for num in arr:
            diff = num - last_num - 1
            if k_index + diff >= k:
                return last_num + (k - k_index)
            last_num = num
            k_index += diff

        return arr[-1] + (k - k_index)
