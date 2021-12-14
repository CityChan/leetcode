class Solution:
    def minKnightMoves(self, target_x, target_y):
        visited = set([(0, 0)])
        queue = collections.deque([(0, 0, 0)])  # (x, y, step)
        directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        
        while queue:
            
            x, y, step = queue.popleft()
            if (x, y) == (target_x, target_y):
                return step
            
            step += 1
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, step))
                    visited.add((new_x, new_y))

