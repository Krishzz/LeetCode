class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [int(nums) for nums in sorted([str(num) for num in range(1,n+1)])]
        return res