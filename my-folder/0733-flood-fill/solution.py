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
        
        q = [(sr, sc)]
        image[sr][sc]=newColor
        while q:
            r, c = q.pop(0)
            # image[r][c]=newColor
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nxt_r, nxt_c = r+d[0], c+d[1]
                if 0<=nxt_r<m and 0<=nxt_c<n and image[nxt_r][nxt_c]==oldColor:
                    image[nxt_r][nxt_c]=newColor
                    q.append((nxt_r, nxt_c))
        return image
        
