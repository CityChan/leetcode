class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        def dfs(image, r, c):
            if 0<=r<m and 0<=c<n and image[r][c]==oldColor:
                image[r][c]=newColor
                for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    dfs(image, r+d[0], c+d[1])
        dfs(image, sr, sc)
        return image
        
