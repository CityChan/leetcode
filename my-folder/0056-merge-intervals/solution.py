class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        res = []
        res.append(intervals[0])
        for i in range(1,n):
            curr = intervals[i]
            start = curr[0]
            end = curr[1]
            
            prev = res[-1]
            start_p = prev[0]
            end_p = prev[1]
            
            if start <= end_p:
                res[-1][1] = max(end_p,end)
            else:
                res.append(curr)
        return res

    
