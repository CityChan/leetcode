# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.max_height(root)
        return self.maxDiameter
        
    def max_height(self, root):
        if root is None:
            return 0
        left_height = self.max_height(root.left)
        right_height = self.max_height(root.right)
        self.maxDiameter = max(self.maxDiameter, left_height + right_height)
        return max(left_height, right_height) + 1
