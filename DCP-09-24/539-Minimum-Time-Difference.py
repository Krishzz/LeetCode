class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = sorted([int(timePoint[0:2])*60+int(timePoint[3:]) for timePoint in timePoints])
        result = 1440+arr[0]-arr[len(arr)-1]
        for i in range(1,len(arr)):
            result = min(result,(arr[i]-arr[i-1]))
        return result

