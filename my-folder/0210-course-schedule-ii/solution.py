class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.buildgraph(numCourses, prerequisites)
        self.onPath = [False]*numCourses
        self.hasCycle = False
        self.visited = [False]*numCourses
        self.postorder = []
        for i in range(numCourses):
            self.traverse(numCourses,i)
        if self.hasCycle:
            return []
        self.postorder.reverse()
        return self.postorder
        
    def traverse(self, numCourses, s):
        if self.onPath[s]:
            self.hasCycle = True
            
        if self.hasCycle or self.visited[s]:
            return 
        
        self.onPath[s] = True
        self.visited[s] = True

        
        for t in self.graph[s]:
            self.traverse(numCourses,t)
        
        self.postorder.append(s)
        self.onPath[s] = False
        
    def buildgraph(self, numCourses, prerequisites):
        self.graph = []
        for i in range(numCourses):
            self.graph.append([])
            
        for item in prerequisites:
            s = item[1]
            t = item[0]
            self.graph[s].append(t)
        
        
