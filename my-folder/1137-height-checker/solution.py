from collections import Counter
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counter = Counter(heights)
        
        i = 0
        result = 0
        for height in heights:
            while counter[i] == 0:
                i += 1
            
            if i != height:
                result += 1
            
            counter[i] -= 1
        return result
