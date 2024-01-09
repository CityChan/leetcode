class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_freq_dict = {}
        s = 0
        for i in nums:
            num_freq_dict[i] = num_freq_dict.get(i, 0)+1
        for i in num_freq_dict:
            if i<k/2:
                s+=min(num_freq_dict[i], num_freq_dict.get(k-i, 0))
            elif i==k/2:
                s+=num_freq_dict[i]//2
        return s
        
