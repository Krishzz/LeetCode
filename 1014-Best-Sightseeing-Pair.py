class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        stk = 0
        prev = values[0]
        for i in range(1, len(values)):
            stk = max(stk, prev+values[i]-i)
            prev = max(prev, values[i]+i)
        return stk