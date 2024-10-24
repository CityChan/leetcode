# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.nodes = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.nodes.append(node.val)
            inorder(node.right)
        inorder(root)
    def next(self) -> int:
        val = self.nodes.pop(0)
        return val
        


    def hasNext(self) -> bool:
        if self.nodes:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
