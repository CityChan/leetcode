class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # print(asteroids)
        for i in asteroids:
            if i<0:
                # print("11")
                flag = 0
                while len(stack)>0:
                    top = stack[-1]
                    if top>0:
                        if top+i<0:
                            stack.pop()
                        elif top+i==0:
                            flag = 1
                            stack.pop()
                            break
                        else:
                            flag = 1
                            break
                    else:
                        break
                if flag==0:
                    stack.append(i)
            else:
                # print("22")
                stack.append(i)
            # print(stack)
        return stack
        
