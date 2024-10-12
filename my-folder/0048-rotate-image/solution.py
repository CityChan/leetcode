class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(i):
                temp =  matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        for i in range(m):
            matrix[i].reverse()
            
        return matrix
