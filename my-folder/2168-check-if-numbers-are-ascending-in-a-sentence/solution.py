class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        prev = -1
        for i in s.split():
            if i.isdigit():
                if int(i)<=prev:
                    return False
                else:
                    prev = int(i)
        return True
        
