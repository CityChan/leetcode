class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bfs = collections.deque([(0, 0, 0)]) 
        visited = set([(0,0)])
        directions = [(2,1),(2,-1),(-2,1),(-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        if x==0 and y==0:
            return 0
        while bfs:
            a, b, step = bfs.popleft()
            if (a, b) == (x, y):
                return step
            step+=1
            for j in directions:
                ii = a+j[0]
                jj = b+j[1]
  
                if (ii, jj) not in visited:
                    bfs.append((ii, jj, step))
                    visited.add((ii, jj))
       
        return -1
            

#         visited = set([(0, 0)])
#         queue = collections.deque([(0, 0, 0)])  # (x, y, step)
#         directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        
#         while queue:
            
#             x, y, step = queue.popleft()
#             if (x, y) == (target_x, target_y):
#                 return step
            
#             step += 1
            
#             for dx, dy in directions:
#                 new_x, new_y = x + dx, y + dy
#                 if (new_x, new_y) not in visited:
#                     queue.append((new_x, new_y, step))
#                     visited.add((new_x, new_y))

    
        
