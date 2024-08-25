class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window_size = sum(data)
        if window_size == 0:
            return 0
        n = len(data)
        res = float('inf')
        left,right = 0, 0
        window_count  = 0
        while right < n:
            if data[right] == 0:
                window_count += 1
            if right - left + 1 >= window_size:
                res = min(res, window_count)
                if data[left] == 0:
                    window_count -= 1
                left += 1
            right +=1
        return res
                    
