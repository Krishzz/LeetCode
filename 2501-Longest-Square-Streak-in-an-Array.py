class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        max_len = -1
        sets = set(nums)
        sorted_sets = sorted(sets)
        for num in sorted_sets:
            count = 0
            curr = num
            while curr in sets:
                sets.remove(curr)
                curr = curr**2
                count+=1
            max_len = max(max_len, count)
        return max_len if max_len>1 else -1