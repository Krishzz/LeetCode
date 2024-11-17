class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i]+nums[i]
        dq = deque()
        min_len = float('inf')
        for i in range(n+1):
            while dq and prefix[i]-prefix[dq[0]]>=k:
                min_len = min(min_len, i - dq.popleft())
            while dq and prefix[i]<=prefix[dq[-1]]:
                dq.pop()
            dq.append(i)
        return min_len if min_len!=float('inf') else -1