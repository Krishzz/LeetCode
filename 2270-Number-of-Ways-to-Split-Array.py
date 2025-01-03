class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        leftsidesum = 0
        rightsidesum = sum(nums)
        validsplits = 0

        for i in range(len(nums)-1):
            leftsidesum+=nums[i]
            rightsidesum-=nums[i]
            if leftsidesum>=rightsidesum:
                validsplits+=1
        return validsplits