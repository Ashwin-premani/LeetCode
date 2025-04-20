class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash = Counter(answers)
        res = 0
        for i,v in hash.items():
            group_size = i + 1
            grps = math.ceil(v/group_size)
            res += grps * group_size
        return res
