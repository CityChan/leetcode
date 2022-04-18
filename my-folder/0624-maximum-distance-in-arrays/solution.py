class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_v = arrays[0][0]
        min_i = 0
        for i in range(len(arrays)):
            if arrays[i][0]<min_v:
                min_v = arrays[i][0]
                min_i = i
        max_i = 0
        max_v = arrays[max_i][-1]
        for i in range(len(arrays)):
            if arrays[i][-1]>max_v:
                max_v = arrays[i][-1]
                max_i = i
        if max_i!=min_i:
            return max_v - min_v
             
        max_i2 = (1 if max_i==0 else 0)
        max_v2 = arrays[max_i2][-1]
        for i in range(len(arrays)):
            if i==max_i:
                continue
            if arrays[i][-1]>max_v2:
                max_v2 = arrays[i][-1]
                max_i2 = i
        min_i2 = (1 if min_i==0 else 0)
        min_v2 = arrays[min_i2][0]
        for i in range(len(arrays)):
            if i==min_i:
                continue
            if arrays[i][0]<min_v2:
                min_v2 = arrays[i][0]
                min_i2 = i
       
        return max(max_v - min_v2, max_v2 - min_v)
