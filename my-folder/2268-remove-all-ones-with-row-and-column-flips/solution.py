class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        front = grid[0]
        back = [1-x for x in grid[0]]
        for i in grid:
            if i!=front and i!=back:
                return False
        return True
        
