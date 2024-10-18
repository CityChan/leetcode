from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pq = []
        for num, feq in counter.items():
            heapq.heappush(pq, (feq, num))
            if len(pq) > k:
                heapq.heappop(pq)
        res = []
        for feq, num in pq:
            res.append(num)
        return res[::-1]
        
        
            
