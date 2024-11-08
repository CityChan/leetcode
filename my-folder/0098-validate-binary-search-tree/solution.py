# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isBST(root, None, None)
    def isBST(self, root, minNode,maxNode):
        if root is None:
            return True
        if minNode is not None and root.val <= minNode.val:
            return False
        if maxNode is not None and root.val >= maxNode.val:
            return False
        return self.isBST(root.left, minNode, root) and self.isBST(root.right, root, maxNode)

