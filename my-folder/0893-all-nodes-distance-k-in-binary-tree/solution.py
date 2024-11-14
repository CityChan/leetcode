# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.ans = []
        self.p = {}
        self.visited = []
        self.parents(root, None)
        self.dfs(target, k)
        return self.ans

    def dfs(self, root, k):
        if root is None or root.val in self.visited:
            return
        self.visited.append(root.val)
        if k == 0:
            self.ans.append(root.val)
            return
        self.dfs(root.left, k - 1)
        self.dfs(root.right, k - 1)
        self.dfs(self.p[root], k - 1)

    def parents(self, root, prev):
        if root is None:
            return
        self.p[root] = prev
        self.parents(root.left, root)
        self.parents(root.right, root)
