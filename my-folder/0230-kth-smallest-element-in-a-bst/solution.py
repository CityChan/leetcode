# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = 0
        self.cnt = 0
        self.traverse(root, k)
        return self.ans
    def traverse(self, root,k):
        if root is None:
            return 
        self.traverse(root.left, k)
        self.cnt += 1
        if self.cnt == k:
            self.ans = root.val
        self.traverse(root.right, k)
        
