class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n-1
        while right>0 and arr[right-1]<=arr[right]:
            right -= 1
        if right == 0:
            return 0
        min_len = right
        for left in range(n):
            if left>0 and arr[left-1]>arr[left]:
                break
            while right<n and arr[left]>arr[right]:
                right+=1
            curr_len = right-left-1
            min_len = min(min_len, curr_len)
        return min_len