class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        res = []
        if n == 1:
            return intervals
        res.append(intervals[0])
        right = intervals[0][1]
        for i in range(1,n):
            a,b = intervals[i][0], intervals[i][1]
            if a <= right:
                right = max(right, b) 
                res[-1][1] = right
            else:
                res.append([a,b])
                right = b
        return res

