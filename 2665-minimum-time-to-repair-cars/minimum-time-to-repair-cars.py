class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 1
        r = max(ranks) * (cars**2)
        while l <= r:
            m = (l+r) // 2
            s = 0
            for i in ranks:
                n = int(math.sqrt(m/i))
                s += n
            if s >= cars:
                r = m - 1
            else:
                l = m + 1
        return l
