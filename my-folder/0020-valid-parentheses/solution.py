class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {'(': ')', '[': ']', '{': '}'}
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if not stack or mapping[stack.pop()]!=i:
                    return False
        
        return True if not stack else False
        
            
        
