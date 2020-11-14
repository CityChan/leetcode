class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        
        for i in range(1, len(points)):
            prev = points[i-1]
            curr = points[i]
            result += max(abs(prev[0] - curr[0]), abs(prev[1] - curr[1]))
            
        return result
