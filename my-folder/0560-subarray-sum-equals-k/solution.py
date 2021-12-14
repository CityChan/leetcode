class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_dict={0:1}
        s=0
        count = 0
        for i in nums:
            s+=i
            if s-k in sum_dict:
                count+=sum_dict[s-k]
            if s not in sum_dict:
                sum_dict[s]=1
            else:
                sum_dict[s]+=1
                
        return count
            
            
        
