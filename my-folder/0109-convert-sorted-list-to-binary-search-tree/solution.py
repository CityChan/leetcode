# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        n = len(nodes)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(val = nodes[0].val)
        mid = n // 2
        nodes[mid-1].next = None
        left_tree = self.sortedListToBST(head)
        right_tree = self.sortedListToBST(nodes[mid].next)
        root = TreeNode(val = nodes[mid].val)
        root.left = left_tree
        root.right = right_tree
        return root
