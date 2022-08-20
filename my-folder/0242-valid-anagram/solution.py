class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        for i in s:
            if i in dict_s:
                dict_s[i]+=1
            else:
                dict_s[i]=1
        for i in t:
            if i not in dict_s:
                return False
            else:
                dict_s[i]-=1
        for i in dict_s:
            if dict_s[i]!=0:
                return False
        return True
        
