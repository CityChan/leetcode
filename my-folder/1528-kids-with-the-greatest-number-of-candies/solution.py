class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i_max = 0
        for i in range(len(candies)):
            if candies[i]>=candies[i_max]:
                i_max = i
        return [x+extraCandies>=candies[i_max] for x in candies]
        
