# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while 1:
            if root.val > max(p.val, q.val):
                root = root.left
            elif root.val < min(p.val, q.val):
                root = root.right
            else:
                return root
        
        


# class unionfind:
#     def __init__(self, n):
#         self.p = list(range(n))
#         self.size = [1 for _ in range(n)]
    
#     def find(self, x):
#         while self.p[x] != x:
#             self.p[x] = self.find(self.p[x])
#         return self.p[x]

#     def union(self, x, y):
#         px, py = self.find(x), self.find(y)
#         if px == py:
#             return False
#         else:
#             if self.size[px] >= self.size[py]:
#                 self.p[y] = px
#                 self.size[px] = self.size[px] + self.size[py]
#             else:
#                 self.p[x] = py
#                 self.size[py] = self.size[py] + self.size[px]
#             return True

