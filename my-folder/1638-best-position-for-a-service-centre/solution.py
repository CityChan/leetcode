class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)
        eps = 1e-6
        decay = 0.999
        alpha = 0.5
        x = y = 0
        for x1,y1 in positions:
            x += x1
            y += y1
        x = x / n
        y = y / n
        while True:
            grad_x = grad_y = 0
            dist = 0
            for x1, y1 in positions:
                a = x - x1
                b = y - y1
                c = sqrt(a*a + b*b)
                grad_x += a / (c + 1e-8)
                grad_y += b / (c + 1e-8)
                dist += c
            dx = grad_x*alpha
            x = x - dx
            dy = grad_y*alpha
            y = y - dy
            alpha = alpha*decay
            if abs(dx) <= eps and abs(dy) <= eps:
                return dist
        
