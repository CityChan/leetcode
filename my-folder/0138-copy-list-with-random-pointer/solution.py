"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dict = {}
        prev = None
        node = head
        
        while node:
            if node not in dict:
                dict[node] = Node(node.val, node.next, node.random)
            if prev:
                prev.next = dict[node]
            else:
                head = dict[node]
            if node.random:
                if node.random not in dict:
                    dict[node.random] = Node(node.random.val, node.random.next, node.random.random)
                dict[node].random = dict[node.random]
            
            prev = dict[node]
            node = node.next
        
        return head
