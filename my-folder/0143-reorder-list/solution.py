# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ans = []
        stk = []
        cur = head
        while cur:
            stk.append(cur)
            cur = cur.next
        count = 0
        while stk:
            if count%2 == 0:
                ans.append(stk[0])
                stk.pop(0)
            else:
                ans.append(stk[-1])
                stk.pop()
            count += 1
        for i in range(len(ans)-1):
            ans[i].next = ans[i+1]
        ans[-1].next = None
        return ans[0]
