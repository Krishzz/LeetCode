class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = mul = 0
        val = inf
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                ans+=abs(matrix[i][j])
                val = min(val, abs(matrix[i][j]))
                if matrix[i][j] < 0:
                    mul^=1
        return ans-2*mul*val