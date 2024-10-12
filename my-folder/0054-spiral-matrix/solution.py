class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        visited = []
        visited_node = 0
        cur = [0,0]
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        dir_num = 0
        ans = []
        while visited_node < m*n:
            visited_node += 1
            i,j = cur[0],cur[1]
            visited.append((i,j))
            ans.append(matrix[i][j])
            cur[0], cur[1] = i + dirs[dir_num][0], j + dirs[dir_num][1]
            if cur[0] < 0 or cur[0] >= m or cur[1] < 0 or cur[1] >= n or (cur[0],cur[1]) in visited:
                dir_num = (dir_num + 1) % 4
                cur[0], cur[1] = i + dirs[dir_num][0], j + dirs[dir_num][1]
        return ans
            
        
            
        
