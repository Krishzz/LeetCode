class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        nums = [-num for num in nums]
        heapify(nums)
        while k:
            tmp = heappop(nums)
            ans-=tmp
            heappush(nums, floor(tmp/3))
            k-=1
        return ans