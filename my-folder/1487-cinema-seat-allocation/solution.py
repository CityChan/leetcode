class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reservedSeats.sort(key = lambda x:x[0])
        count = 2*n
        i = 0
        while i<len(reservedSeats):
            cur = set()
            # row = reservedSeats[i][0]
            j = i
            while 1:
                if j>=len(reservedSeats):
                    break
                if reservedSeats[j][0]==reservedSeats[i][0]:
                    cur.add(reservedSeats[j][1])
                else:
                    break
                j+=1
            i=j
            now_count = 0
            if all(x not in cur for x in (2,3,4,5)):
                now_count+=1
            if all(x not in cur for x in (6,7,8,9)):
                now_count+=1
            if all(x not in cur for x in (4,5,6,7)) and now_count==0:
                now_count=1
            count+=now_count-2
        return count
            
