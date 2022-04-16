class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1]) #' '.join(s.lstrip(' ').rstrip(' ').split(' ')[::-1])
        
