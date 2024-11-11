# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum = 0
        self.res = []
        if root is None:
            return 0
        self.traverse(root,"")
        print(self.res)
        for res in self.res:
            sum += int(res)
        return sum
    
    def traverse(self, root, track):
        track += str(root.val)
        if root.left is None and root.right is None:
            self.res.append(track)
        if root.left:
            self.traverse(root.left, track)
        if root.right:
            self.traverse(root.right, track)
        
