class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        stack = []
        for i, e in enumerate(s):
            if e=='(':
                stack.append(i)
            elif e==')':
                if stack:
                    stack.pop()
                else:
                    s[i]=''
        for e in stack:
            s[e]=''
        return ''.join(s)
            
        
