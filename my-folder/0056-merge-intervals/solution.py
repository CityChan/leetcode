class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x:x[0])
        res = [intervals[0]]

        for i in intervals[1:]:

            if i[0]<=res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], i[1])]
            else:
                res.extend([i])
        return res
        
