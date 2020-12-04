# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode(None)
        k = len(lists)
        queue = PriorityQueue(maxsize=k)
        
        for list_idx, node in enumerate(lists):
            if node:
                queue.put((node.val, list_idx, node))
        
        while queue.qsize() > 0:
            poped = queue.get()
            curr.next = poped[2]
            list_idx = poped[1]
            curr = curr.next
            
            if curr.next:
                queue.put((curr.next.val, list_idx, curr.next))
        
        return dummy.next
        
