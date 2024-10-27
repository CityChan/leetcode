# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = {}
        self.traverse(root, 0)
        for val in self.ans:
            if val%2:
                self.ans[val].reverse()
        return list(self.ans.values())
    def traverse(self, root, depth):
        if root is None:
            return
        if depth not in self.ans:
            self.ans[depth] = []
        self.ans[depth].append(root.val)
        self.traverse( root.left, depth+1)
        self.traverse( root.right, depth+1)
        
