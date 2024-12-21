class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ij = res = 0
        dic = dict()
        for i in range(len(nums)):
            d_copy = dic.copy()
            for k,v in d_copy.items():
                if abs(k-nums[i])>2:
                    ij = max(ij, v+1)
                    dic.pop(k)
            dic[nums[i]] = i
            res+=i-ij+1
        return res