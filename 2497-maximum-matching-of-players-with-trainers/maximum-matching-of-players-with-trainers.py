class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        res = 0
        i = 0
        j = 0
        n = len(players)
        m = len(trainers)
        while i < n and j < m:
            if players[i] <= trainers[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res