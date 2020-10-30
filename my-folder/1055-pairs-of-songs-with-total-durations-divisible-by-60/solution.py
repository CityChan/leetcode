class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        # create an array of 60 elements with init value 0
        counter = [0] * 60

        for i in time:
            res = res + counter[- i % 60]
            counter[i % 60] = counter[i % 60] + 1

        return res
