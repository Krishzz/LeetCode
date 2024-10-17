class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(i) for i in str(num)]
        for i in range(len(num)-1):
            max_num = max(num[i+1:])
            if num[i]<max_num:
                for j in range(len(num)-1, i, -1):
                    if num[j] == max_num:
                        break
                num[i], num[j] = num[j], num[i]
                break
        return int(''.join([str(i) for i in num]))

        