class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hashset = set()
        arr1, arr2 = [str(num) for num in arr1], [str(nums) for nums in arr2]
        res = 0
        for num1 in arr1:
            prefix = ""
            for digit in num1:
                prefix+=digit
                hashset.add(prefix)
        for num2 in arr2:
            prefix = ""
            temp = 0
            for dig in num2:
                prefix+=dig
                if prefix in hashset:
                    temp+=1
            res = max(res, temp)
        return res