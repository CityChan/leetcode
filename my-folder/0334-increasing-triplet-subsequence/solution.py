class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
                
        from collections import deque
        
        stack = deque([nums[0]])
        for n in nums[1:]:
            if len(stack)==1:
                if n>stack[-1]:
                    stack.append(n)
                else:
                    stack[-1]=n
            elif len(stack)==2:
                if n>stack[-1]:
                    return True
                elif n>stack[0]:
                    stack[-1]=n
                else:
                    stack.append(n)
            elif len(stack)==3:
                if n>stack[1]:
                    return True
                elif n>stack[-1]:
                    stack.popleft()
                    stack.popleft()
                    stack.append(n)
                else:
                    stack[-1]=n
        return False
        
