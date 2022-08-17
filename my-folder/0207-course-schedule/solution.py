class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre_dict = [set() for _ in range(numCourses)]
        for i in prerequisites:
            pre_dict[i[0]].add(i[1])
        
        visited = [0]*numCourses
        
        def dfs(course):
            if visited[course]==1:
                return True
            if visited[course]==-1:
                return False

            visited[course]=-1
            for c in pre_dict[course]:
                if not dfs(c):
                    return False
            visited[course]=1
            return True   
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True        
                
        
