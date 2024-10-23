class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.create_adjaceny_list(edges)
        return self.hasPath(graph, source, destination, set())
    def hasPath(self, graph, source, destination, visited):
        if source == destination: return True
        if source in visited: return False
        visited.add(source)
        for ele in graph[source]:
            if self.hasPath(graph, ele, destination, visited) == True:
                return True
        return False
    
    def create_adjaceny_list(self, edges):
        graph = {}
        for a,b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph