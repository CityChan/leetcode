# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        count = 0
        while l1:
            num1+= l1.val*10**count
            count+=1
            l1 = l1.next
        
        count = 0       
        while l2:
            num2+= l2.val*10**count
            count+=1
            l2 = l2.next
        num = num1 + num2
        print(num)
        head = ListNode(0)
        cur = ListNode(num%10)
        head.next = cur
        num = num // 10
        while num:
            node = ListNode(num%10)
            cur.next = node
            cur = node
            num = num // 10
        return  head.next
