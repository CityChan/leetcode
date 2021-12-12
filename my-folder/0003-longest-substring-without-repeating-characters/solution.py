class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        save_dict = {s[0]: 0}
        start, end = 0, 1
        max_len = 1
        while end<len(s):
            if (s[end] in save_dict) and (save_dict[s[end]]>=start):
                start = save_dict[s[end]] + 1
                           
            save_dict[s[end]] = end
            max_len = max(max_len, end-start+1)
            
            end+=1
            
        return max_len
            
        
