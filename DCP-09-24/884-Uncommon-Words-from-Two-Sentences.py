class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3=(s1+" "+s2).split(" ")
        ar = []
        for x in s3:
            if s3.count(x) == 1:
                ar.append(x)
        return(ar)