class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if total>0:
                    k-=1
                elif total<0:
                    j+=1
                else:
                    triplets.add((nums[i], nums[j], nums[k]))
                    k-=1
                    j+=1
        return triplets
