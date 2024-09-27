class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        n1 = 0
        n2 = 1
        for i in range(n):
            res = n1+n2
            n1,n2 = n2, res
        return n2