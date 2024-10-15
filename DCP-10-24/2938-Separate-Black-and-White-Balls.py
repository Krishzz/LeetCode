class Solution:
    def minimumSteps(self, s: str) -> int:
        ct, zeros = 0,0
        for c in s:
            if c == "0":
                ct+=zeros
            else:
                zeros+=1
        return ct