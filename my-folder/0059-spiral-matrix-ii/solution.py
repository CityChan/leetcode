class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        output = [[0]*n for i in range(n)]
        count = 1
        num = (n+1)//2
        for layer in range(num):
            for i in range(layer, n-layer):
                output[layer][i] = count
                count+=1
            for i in range(layer+1, n-layer):
                output[i][n-layer-1] = count
                count+=1
            for i in range(n-layer-2, layer-1, -1):
                output[n-layer-1][i] = count
                count+=1
            for i in range(n-layer-2, layer, -1):
                output[i][layer] = count
                count+=1
        return output
            
            
            
            
        
