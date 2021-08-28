class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        out = []
        for i in sorted(intervals, key=lambda j: j[0]):
            if len(out)==0 or i[0]>out[-1][1] :
                out+=i,
            else:
                out[-1] = [out[-1][0], max(out[-1][1], i[1])]
        return out

