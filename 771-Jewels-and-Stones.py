class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for item in set(jewels):
            count+=stones.count(item)
        return count