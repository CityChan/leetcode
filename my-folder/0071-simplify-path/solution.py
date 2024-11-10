class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stk = []
        for v in parts:
            if v == "..":
                if stk:
                    stk.pop()
            elif v == "." or v =="":
                continue
            else:
                stk.append(v)
        return "/" + "/".join(stk)
