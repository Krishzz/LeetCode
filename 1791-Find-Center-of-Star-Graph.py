class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = self.create_adjacency_list(edges)
        graph = sorted(graph, key=lambda x:len(graph[x]), reverse=True)
        return graph[0]
        
    def create_adjacency_list(self, edges):
        graph = {}
        for a,b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        return graph
