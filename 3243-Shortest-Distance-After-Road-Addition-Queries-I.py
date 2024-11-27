class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]
        print(adj)
        def bfs():
            q = deque()
            q.append((0,0))
            visit = set()
            visit.add((0,0))
            while q:
                cur, length = q.popleft()
                if cur == n-1:
                    return length
                for neighbor in adj[cur]:
                    if neighbor not in visit:
                        q.append((neighbor, length+1))
                        visit.add(neighbor)
        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(bfs())
        return res