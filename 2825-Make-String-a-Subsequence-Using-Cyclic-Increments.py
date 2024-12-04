class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx, lens = 0, len(str2)
        for char in str1:
            if idx<lens and (ord(str2[idx])-ord(char))%26<2:
                idx+=1
        return idx == lens