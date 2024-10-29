# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        cnt = 0
        n = len(s)
        if n == 0:
            return None
        indices = []
        start, end = 0, 0
        head_index = 0
        while head_index < n and s[head_index] != '(' :
            head_index += 1
        head_num = s[:head_index]
        head_num = int(head_num)
        head = TreeNode(val = head_num)
        for i in range(len(s)):
            if s[i] == "(":
                cnt += 1
                if cnt == 1:
                    start = i+1
            if s[i] == ")":
                cnt -= 1
                if cnt == 0:
                    end = i
                    indices.append([start, end])
                    start, end = 0, 0
        for start, end in indices:
            child = self.str2tree(s[start:end])
            if head.left is None:
                head.left = child
            else:
                head.right = child
        return head
