class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.k = k
        self.n = n
        self.backtrack(1,[])
        return self.res
        
    def backtrack(self, start, track):
        if len(track) == self.k:
            self.res.append(copy.deepcopy(track))
            return
        for i in range(start, self.n+1):
            track.append(i)
            self.backtrack(i+1,track)
            track.pop()
            
        return
