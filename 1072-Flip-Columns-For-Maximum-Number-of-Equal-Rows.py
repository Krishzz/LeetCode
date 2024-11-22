class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = Counter()
        for ele in matrix:
            ar = tuple(ele) if ele[0]==0 else tuple(bit^1 for bit in ele)
            rows[ar]+=1
        return max(rows.values())