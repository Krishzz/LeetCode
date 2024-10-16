class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        arr = sorted([[a, 'a'], [b, 'b'], [c, 'c']], reverse=True)
        st = ''
        k = max(0, arr[0][0]-2 * arr[1][0])
        for i in range(arr[1][0]):
            st+=(1+(i<arr[0][0]-arr[1][0]))*arr[0][1]+arr[1][1]
            if i<arr[2][0]:
                st+= min(2,k)*arr[0][1]+arr[2][1]
                k-=min(2,k)
        return st+min(2,k)*arr[0][1]