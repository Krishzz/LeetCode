class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adj_list = {i:[] for i in range(len(vals))}
        for src, dst in edges:
            adj_list[src].append(vals[dst])
            adj_list[dst].append(vals[src])
        ans = -inf
        for src in adj_list:
            curr = vals[src]
            min_heap = []
            for val in adj_list[src]:
                if val > 0:
                    heappush(min_heap, val)
                    curr += val
                    if len(min_heap) > k:
                        curr -= heappop(min_heap)
            ans = max(ans, curr)
        return ans
    
    def create_adjaceny_list(self, edges, vals):
        graph = {}
        for a,b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(vals[b])
            graph[b].append(vals[a])
        return graph

        