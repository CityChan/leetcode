"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        dummpy = Node(0, None, head, None)
        self.preorder(dummpy, head)
        dummpy.next.prev = None
        return dummpy.next
    
    def preorder(self, prev, cur):
        if cur is None:
            return prev
        cur.prev = prev
        prev.next = cur

        t = cur.next
        tail = self.preorder(cur, cur.child)
        cur.child = None
        return self.preorder(tail, t)

