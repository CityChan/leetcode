class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        diff = [0]*1001
        for t in trips:
            diff[t[1]]+=t[0]
            diff[t[2]]-=t[0]
        s = 0
        for i in diff:
            s+=i
            if s>capacity:
                return False
        return True
