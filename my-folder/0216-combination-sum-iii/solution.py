class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def traverse(current_res, s, i):
            if len(current_res)==k and s == n:
                res.append(current_res)
            elif i<=9 and len(current_res)<k and i<=n-s:
                traverse(current_res+[i], s+i, i+1)
                traverse(current_res, s, i+1)
            # print(current_res)
        traverse([], 0, 1)
        return res
            
