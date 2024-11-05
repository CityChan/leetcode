class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        return n - self.intervalSchedule(intervals)

    def intervalSchedule(self, intvs):
        if not intvs:
            return 0
        intvs.sort(key = lambda x: x[1])
        count = 1
        x_end = intvs[0][1]
        for interval in intvs:
            start = interval[0]
            if start >= x_end:
                count += 1
                x_end = interval[1]
        return count

