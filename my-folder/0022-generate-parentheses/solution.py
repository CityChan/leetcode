class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
    #         def generate(p, left, right, parens=[]):
    #     if left:         generate(p + '(', left-1, right)
    #     if right > left: generate(p + ')', left, right-1)
    #     if not right:    parens += p,
    #     return parens
    # return generate('', n, n)
        
        res = []
        def traverse(now, left, right):
            if left+right==2*n:
                res.append(now)
            if left<n:
                traverse(now+"(", left+1, right)
            if right<left:
                traverse(now+")", left, right+1)
        traverse("", 0, 0)
        return res
