class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl = 0
        tl = 0
        while sl<len(s) and tl<len(t):
            if s[sl] == t[tl]:
                sl+=1
            tl+=1
        return sl == len(s)