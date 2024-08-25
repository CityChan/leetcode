class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        avaiable = [intervals[0][1]]
        res = 1
        n = len(intervals)
        for i in range(1,n):
            start = intervals[i][0]
            end = intervals[i][1]
            min_avai = min(avaiable)
            if start < min_avai:
                avaiable.append(end)
            else:
                avaiable.remove(min_avai)
                avaiable.append(end)
            res = max(res, len(avaiable))
        return res

