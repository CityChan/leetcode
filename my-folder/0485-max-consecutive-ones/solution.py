class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        answer = 0
        for num in nums:
            if num == 1:
                count += 1
                answer = max(answer, count)
            else:
                count = 0
        return answer
