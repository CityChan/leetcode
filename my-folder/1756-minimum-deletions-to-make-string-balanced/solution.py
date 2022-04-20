class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_b = 0
        res = 0
        for char in s:
            if char=='a':
                res = min(res+1, count_b)
            else:
                count_b+=1
        return res
        
