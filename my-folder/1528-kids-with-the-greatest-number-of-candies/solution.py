class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [True] * len(candies)
        max = candies[0]
        for i in range(1, len(candies)):
            if candies[i] > max:
                max = candies[i]
                
        for j in range(len(candies)):
            if candies[j] == max or candies[j] + extraCandies >= max:
                result[j] = True
            else:
                result[j] = False
        return result
