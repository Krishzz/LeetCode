class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(st, visited):
            if st==len(s):
                return 0
            maxs = 0
            for en in range(st+1, len(s)+1):
                sub = s[st:en]
                if sub not in visited:
                    visited.add(sub)
                    maxs = max(maxs, 1+dfs(en,visited))
                    visited.remove(sub)
            return maxs
        return dfs(0, set())
        