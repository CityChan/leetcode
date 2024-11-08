"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.map = defaultdict(list)
        self.traverse(root, 0)
        for key in self.map:
            layer = self.map[key]
            for i in range(len(layer)-1):
                layer[i].next = layer[i+1]
        return root

    def traverse(self,root, depth):
        if root is None:
            return
        self.map[depth].append(root)
        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)
