class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        ans = 1
        available = [intervals[0][1]]
        for start, end in intervals[1:]:
            if start < min(available):
                ans += 1
            else:
                heapq.heappop(available)
            heapq.heappush(available, end)
            print(available)


        return ans
