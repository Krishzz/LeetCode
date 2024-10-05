class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        cur_st = ''
        for st in s2:
            cur_st += st
            if len(cur_st) == len(s1):
                if ''.join(sorted(cur_st)) == s1:
                    return True
                cur_st = cur_st[1:]
        return False