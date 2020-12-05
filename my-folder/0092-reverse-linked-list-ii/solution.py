# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        prev = dummyNode

        for i in range(m-1):
            prev = prev.next

        # reverse the [m,n] nodes
        reverse = None
        curr = prev.next
        for i in range(n-m+1):
            next = curr.next
            curr.next = reverse
            reverse = curr
            curr = next

        prev.next.next = curr
        prev.next = reverse

        return dummyNode.next
