# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = [root]
        depth = 0
        while q:
            sz = len(q)
            depth += 1
            for _ in range(sz):
                now = q.pop(0)
                if now.left is not None:
                    q.append(now.left)
                if now.right is not None:
                    q.append(now.right)
        return depth
        
