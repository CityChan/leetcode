# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self.target = targetSum
        self.traverse(root, 0, [])
        return self.ans
    def traverse(self, root, sum, subtree):
        if root is None:
            return None
        sum += root.val
        subtree.append(root.val)
        if sum == self.target and root.left is None and root.right is None:
            self.ans.append(subtree)
        self.traverse(root.left, sum, copy.deepcopy(subtree))
        self.traverse(root.right, sum, copy.deepcopy(subtree))
