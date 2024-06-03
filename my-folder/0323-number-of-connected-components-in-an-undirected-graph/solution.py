class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connect_dict = {i:set() for i in range(n)}
        for i, j in edges:
            connect_dict[i].add(j)
            connect_dict[j].add(i)
        
        
        count = 0
        visited = set()
        for start_node in connect_dict:
            # print(start_node)
            if start_node not in visited:
                count+=1
                q = [start_node]
                visited.add(start_node)
                while q:
                    cur_node = q.pop(0)
                    # visited.add(cur_node)
                    for next_node in connect_dict[cur_node]:
                        if next_node not in visited:
                            q.append(next_node)
                            visited.add(next_node)
        
        return count
                
        
