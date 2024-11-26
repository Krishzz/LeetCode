class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        isundef = [True]*n
        for winner, loser in edges:
            isundef[loser] = False
        champion = -1
        champcount = 0
        for team in range(n):
            if isundef[team]:
                champion = team
                champcount+=1
        if champcount == 1:
            return champion
        return -1