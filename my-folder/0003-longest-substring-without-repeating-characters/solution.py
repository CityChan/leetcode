class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        res=s[0]
        temp_res=s[0]
        left, right = 0, 1
        while right<len(s):
            temp = temp_res.find(s[right])
            if temp==-1:
                temp_res+=s[right]
            else:
                left=right-len(temp_res)+temp+1
                if len(temp_res)>len(res):
                    res=temp_res
                temp_res=s[left:right+1]
            right+=1
        return max(len(res), len(temp_res))
                
                
        
