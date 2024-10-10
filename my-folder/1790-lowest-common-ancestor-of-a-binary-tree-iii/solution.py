"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        cur1, cur2 = p, q
        while cur1 != cur2:
            cur1 = cur1.parent if cur1.parent else q
            cur2 = cur2.parent if cur2.parent else p
        return cur1
