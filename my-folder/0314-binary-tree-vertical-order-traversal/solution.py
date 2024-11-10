# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = defaultdict(list)
        self.traverse(root, 0, 0)
        ans = list(self.ans.items())
        ans.sort(key = lambda x: x[0])
        ans = [item[1] for item in ans]
        res = []
        for v in ans:
            a = [val[0] for val in v]
            res.append(a)
        return res

    def traverse(self, root, offset, depth):
        if root is None:
            return 
        self.ans[offset].append([root.val, depth])
        self.ans[offset].sort(key = lambda x: x[1])
        self.traverse(root.left, offset-1, depth + 1)
        self.traverse(root.right, offset+1, depth + 1)


        
