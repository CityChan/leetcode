class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = 0
        max_a = 0
        for i in gain:
            s+=i
            max_a = max(max_a, s)
        return max_a
        
