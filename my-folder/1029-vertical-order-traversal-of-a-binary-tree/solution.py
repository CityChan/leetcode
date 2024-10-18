# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = {}
        self.traverse(root, 0,0)
        keys = sorted(self.ans)
        ans = []
        for key in keys:
            self.ans[key].sort(key = lambda x: (x[1], x[0]))
            res = []
            for t,_ in self.ans[key]:
                res.append(t)
            ans.append(res)
        return ans
    
    def traverse(self, root, offset,depth):
        if root is None:
            return
        if offset in self.ans:
            self.ans[offset].append((root.val, depth))
        else:
            self.ans[offset] = [(root.val, depth)]
        self.traverse(root.left, offset - 1, depth+1)
        self.traverse(root.right, offset + 1,depth+1)
        return
