class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l<r:
            mid = (l+r)//2
            if sum((n-1)// mid for n in nums)<=maxOperations:
                r = mid
            else:
                l = mid+1
        return r
