# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        others = head.next.next
        p2.next = p1
        p1.next = self.swapPairs(others)
        return p2

