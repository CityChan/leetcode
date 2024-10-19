class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i,j = 0, 0
        while i < len(firstList) and j < len(secondList):
            a1,a2 = firstList[i][0], firstList[i][1]
            b1,b2 = secondList[j][0], secondList[j][1]
            
            if b2 >= a1 and a2 >= b1:
                res.append([max(a1,b1), min(a2,b2)])
            if b2 < a2:
                j += 1
            else:
                i += 1
        return res
