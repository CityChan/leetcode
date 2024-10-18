# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = {}
        if root is None:
            return []
        self.ans[0] = [[root.val,0]]
        self.traverse(root, 0, 0)
        ans = []
        for key in self.ans:
            each_layer = self.ans[key]
            ans.append(each_layer[-1][0])
        return ans
        
    def traverse(self, root, offset, depth):
        if root is None:
            return
        if depth in self.ans:
            self.ans[depth].append([root.val, depth])
        else:
            self.ans[depth] = [[root.val, depth]] 
        self.traverse(root.left, offset-1, depth+1)
        self.traverse(root.right, offset+1, depth+1)
        return 
                       
                       
