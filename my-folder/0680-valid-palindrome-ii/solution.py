class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        while left < right:
            if s[left]!=s[right]:
                if s[left+1: right+1]==s[right: left: -1] or \
                s[left: right]==s[-len(s)+right-1: -len(s)+left-1:-1]:
                    return True
                else:
                    return False
            else:
                left+=1
                right-=1
        return True
        
