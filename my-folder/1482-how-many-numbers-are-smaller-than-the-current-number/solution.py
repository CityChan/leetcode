class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         construct a buckets array to count the frequency of each number
        buckets = [0] * 101
        for num in nums:
            buckets[num] += 1
#         convert the counts of num of counts of previous smaller counts 
        prevSmaller = 0
        for i, count in enumerate(buckets):
            if count != 0:
                buckets[i] = prevSmaller
                prevSmaller += count
        
        return [buckets[num] for num in nums]
