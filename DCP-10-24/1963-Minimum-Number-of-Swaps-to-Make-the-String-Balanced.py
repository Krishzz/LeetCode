class Solution:
    def minSwaps(self, s: str) -> int:
        ar = 0
        for i in s:
            if i == '[':
                ar+=1
            elif ar>0:
                ar-=1
        return (ar+1)//2