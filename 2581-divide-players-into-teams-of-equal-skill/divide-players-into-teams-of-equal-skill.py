class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill) - 1
        total_sum = skill[l] + skill[r]
        pairs = []
        
        while l < r:
            if total_sum == (skill[l] + skill[r]):
                pairs.append([skill[l], skill[r]])
            else:
                return -1
            l += 1
            r -= 1
            
        s = 0
        for i in pairs:
            s += (i[0] * i[1])
        return s
