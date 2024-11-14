class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def minMax(prod):
            store = sum((quantity+prod-1)//prod for quantity in quantities)
            return store<=n
        l, r = 1, max(quantities)
        while l<r:
            mid = (l+r)//2
            if minMax(mid):
                r = mid
            else:
                l = mid+1
        return l