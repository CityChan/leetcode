class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        connect_dict = {}
        for i in range(n):
            connect_dict[i] = set()
        for i, j in edges:
            connect_dict[i].add(j)
            connect_dict[j].add(i)
        visited = set()
        count_list = []
        for i in range(n):
            if i not in visited:
                q = [i]
                count = 0
                while q:
                    cur_node = q.pop(0)
                    # if cur_node not in visited:
                    count+=1
                    visited.add(cur_node)
                    for j in connect_dict[cur_node]:
                        if j not in visited:
                            q.append(j)
                            visited.add(j)
                count_list.append(count)
        # print(count_list)
        
#         s = 0
        
#         for i in range(len(count_list)):
#             for j in range(i+1, len(count_list)):
#                 s+=count_list[i]*count_list[j]
                
        return int((sum(count_list)**2-sum([c**2 for c in count_list]))/2)
                
            
        
        
#         def dfs(node):
#             if used_bool[node]==False:
#                 used_bool[node]=True
#                 count=1
#                 for j in to_dict[node]:
#                     count+=dfs(j)
#             else:
#                 count=0
#             return count
        
#         to_dict = {}
#         for i in range(n):
#             to_dict[i] = set()
#         for i, j in edges:
#             to_dict[i].add(j)
#             to_dict[j].add(i)
#         used_bool = [False]*n
#         collect_list = []
#         for i in range(n):
#             if not used_bool[i]:
#                 c = dfs(i)
#                 collect_list.append(c)
#         # print(collect_list)
#         # print(to_dict)
#         # s = 0
#         # for i in range(len(collect_list)):
#         #     for j in range(i+1, len(collect_list)):
#         #         s+=collect_list[i]*collect_list[j]
#         return int((sum(collect_list)**2-sum([c**2 for c in collect_list]))/2)
        
        
# # class Solution(object):
# #     def countPairs(self, n, edges):
# #         neighbors = [[] for _ in range(n)]
# #         for edge in edges:
# #             neighbors[edge[0]].append(edge[1])
# #             neighbors[edge[1]].append(edge[0])

# #         visited = [False] * n
# #         sum_, squaresum = 0, 0

# #         for i in range(n):
# #             if not visited[i]:
# #                 ans = self.dfs(i, neighbors, visited)
# #                 sum_ += ans
# #                 squaresum += ans * ans

# #         return (sum_ * sum_ - squaresum) // 2

# #     def dfs(self, node, neighbors, visited):
# #         visited[node] = True
# #         ans = 1

# #         for neighbor in neighbors[node]:
# #             if not visited[neighbor]:
# #                 ans += self.dfs(neighbor, neighbors, visited)

# #         return ans
