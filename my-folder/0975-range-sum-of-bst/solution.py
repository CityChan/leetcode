# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        self.traverse(root, low, high)
        return self.sum
        
    def traverse(self, root, low, high):
        if root is None:
            return
        if root.val >= low and root.val <= high:
            self.sum += root.val
        self.traverse(root.left, low, high)
        self.traverse(root.right, low, high)
        return
