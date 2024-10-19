"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        self.head = None
        self.prev = None
        self.traverse(root)
        self.prev.right = self.head
        self.head.left = self.prev
        return self.head
        
        
    def traverse(self,root):
        if root is None:
            return
        self.traverse(root.left)
        if self.prev:
            self.prev.right = root
            root.left = self.prev
        else:
            self.head = root
        self.prev = root
        self.traverse(root.right)
        
            
