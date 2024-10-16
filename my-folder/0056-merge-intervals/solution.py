class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        res = []
        res.append(intervals[0])
        for i in range(1, n):
            interval = intervals[i]
            pre_interval = res[-1]
            start, end = interval[0], interval[1]
            pre_start, pre_end = pre_interval[0], pre_interval[1]
            if start <= pre_end:
                res[-1][1] = max(end, pre_end)
            else:
                res.append([start,end])
        return res
    
