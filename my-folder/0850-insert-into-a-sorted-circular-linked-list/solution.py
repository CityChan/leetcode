"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
        prev = head
        cur = head.next
        node = Node(insertVal)
        while cur != head:
            if prev.val <= insertVal <= cur.val:
                break
            if prev.val > cur.val and (insertVal >= prev.val or insertVal <= cur.val):
                break
            prev = cur
            cur = cur.next
        prev.next = node
        node.next = cur
        return head
        
