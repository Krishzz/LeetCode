class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        res = [['.']*rows for _ in range(cols)]
        for row in range(rows):
            i = cols-1
            for col in reversed(range(cols)):
                if box[row][col]=='#':
                    res[i][rows-row-1]='#'
                    i-=1
                elif box[row][col] == '*':
                    res[col][rows-row-1]='*'
                    i=col-1
        return res