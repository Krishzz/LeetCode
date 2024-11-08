class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_bit = (1<<maximumBit)-1
        n = len(nums)
        res = [0]*n
        curr = 0
        for i in range(n):
            curr^=nums[i]
            res[n-i-1] = ~curr&max_bit
        return res