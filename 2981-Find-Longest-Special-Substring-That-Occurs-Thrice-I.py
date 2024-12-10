class Solution:
    def maximumLength(self, s: str) -> int:
        def func(substring):
            return len(set(substring))==1
        max_len = -1
        hash = defaultdict(int)
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if func(substring):
                    hash[substring] +=1
        for x,y in hash.items():
            if y>=3:
                max_len = max(max_len, len(x))
        return max_len