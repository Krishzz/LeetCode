class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limit = {c:s.count(c)-k for c in 'abc'}
        if any(x<0 for x in limit.values()):
            return -1
        count = {c:0 for c in 'abc'}
        ans = l = 0
        for r, c in enumerate(s):
            count[c]+=1
            while count[c]>limit[c]:
                count[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return len(s)-ans