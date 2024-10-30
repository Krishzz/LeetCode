class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        LS = [1]*n
        RS = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    LS[i] = max(LS[i], LS[j]+1)
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    RS[i] = max(RS[i], RS[j]+1)
        max_len = 0
        for i in range(1, n-1):
            if LS[i]>1 and RS[i]>1:
                max_len = max(max_len, LS[i]+RS[i]-1)
        return n-max_len