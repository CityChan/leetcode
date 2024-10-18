# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        if root is None:
            return 0
        self.traverse(root, '')
        return self.sum
    def traverse(self, root, s):
        s += str(root.val)
        if root.left is None and root.right is None:
            self.sum += int(s)
        if root.left:
            self.traverse(root.left, s )
        if root.right:
            self.traverse(root.right, s )
        
