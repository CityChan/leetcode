class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def traverse(now_str, l, r):
            if len(now_str)==2*n:
                res.append(now_str)
            if l<n:
                traverse(now_str+"(", l+1, r)
            if r<l:
                traverse(now_str+")", l, r+1)
        traverse("", 0, 0)
        return res
        
