class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        max_count=0
        count_=0
        i = 0
        j = 0
        while i<len(starts):
            if starts[i]<ends[j]:
                i+=1
                count_+=1
            else:
                j+=1
                max_count=max(max_count, count_)
                count_-=1
        return max(max_count, count_)
        
            
        
