class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """

        def maxSum(nums, nowLen):
            res = [-1 for _ in range(len(nums))]
            s = 0
            for i in range(len(nums)):
                if i<nowLen-1:
                    s+=nums[i]
                elif i==nowLen-1:
                    s+=nums[i]
                    res[i]=s
                else:
                    s = s+nums[i]-nums[i-nowLen]
                    res[i] = max(res[i-1], s)
            return res
        
        first_left = maxSum(nums, firstLen)
        second_left = maxSum(nums, secondLen)
        first_right = maxSum(nums[::-1], firstLen)[::-1]
        second_right = maxSum(nums[::-1], secondLen)[::-1]
        
        max_res = -1
        return max(max([first_left[i]+second_right[i+1] for i in range(len(nums)-1)]),
            max([second_left[i]+first_right[i+1] for i in range(len(nums)-1)]))
