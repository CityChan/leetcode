class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left, st = [-1]*n, []
        for i,v in enumerate(nums):
            while st and nums[st[-1]] >= v: st.pop()
            if st: left[i] = st[-1]
            st.append(i)
        
        right, st = [n]*n, []
        for j in range(n-1, -1, -1):
            while st and nums[st[-1]] >= nums[j]: st.pop()
            if st: right[j] = st[-1]
            st.append(j)
        
        for num, l, r in zip(nums, left, right):
            k = r - l -1
            if num > threshold // k:
                return k
        return -1
