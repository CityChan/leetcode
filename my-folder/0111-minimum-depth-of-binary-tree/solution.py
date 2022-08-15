# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        depth = 1
        q = [root]
        while q:
            sz = len(q)
            for _ in range(sz):
                i = q.pop(0)
                if i.left is None and i.right is None:
                    return depth
                if i.left is not None:
                    q.append(i.left)
                if i.right is not None: 
                    q.append(i.right)
            depth+=1
            
        # return depth  
    
        # def bfs(node):
        #     if node.left is None and node.right is None:
        #         return
        #     elif node.left is not None:
        #         bfs(left)
        #     else:
        #         bfs(right)
        # bfs(root)
        
