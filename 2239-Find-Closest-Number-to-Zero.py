class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        arr = min([abs(num) for num in nums])
        return arr if arr in nums else arr*-1
        