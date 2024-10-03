class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ct_sum =sum(nums)
        rem = ct_sum%p
        if rem == 0:
            return 0
        res = len(nums)
        pre_sum = 0
        hashmap_rem = {0:-1}
        for i in range(len(nums)):
            pre_sum+=nums[i]
            curr_rem = pre_sum%p
            target = (curr_rem-rem)%p
            if target in hashmap_rem:
                res = min(res, i-hashmap_rem[target])
            hashmap_rem[curr_rem] = i
        return res if res<len(nums) else -1