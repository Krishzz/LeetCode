class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)
        end_ptr, grp_ct = 0, 0
        for st in start_times:
            if st>end_times[end_ptr]:
                end_ptr+=1
            else:
                grp_ct+=1
        return grp_ct