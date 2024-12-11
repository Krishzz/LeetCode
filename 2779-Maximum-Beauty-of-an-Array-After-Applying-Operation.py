class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = []
        for num in nums:
            events.append((num-k,1))
            events.append((num+k+1, -1))
        events.sort()
        max_beauty = 0
        curr_count = 0
        for val,eff in events:
            curr_count+=eff
            max_beauty = max(max_beauty, curr_count)
        return max_beauty