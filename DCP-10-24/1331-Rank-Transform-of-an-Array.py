class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ar = sorted(set(arr))
        hashmap = {ar[i]:i+1 for i in range(len(ar))}
        array = [hashmap[j] for j in arr]
        return array