class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        from collections import Counter
        val_list = sorted(Counter(s).values(), reverse = True)
        print(val_list)
        for i in range(len(val_list)-1):
            if val_list[i]<=val_list[i+1]:
                count+=val_list[i+1]-max(val_list[i]-1, 0)
                val_list[i+1] = max(val_list[i]-1, 0)
        return count
        
