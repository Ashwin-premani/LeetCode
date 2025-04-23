class Solution:
    def countLargestGroup(self, n: int) -> int:
        hash = {}

        def sum_of_digits(i):
            return sum(int(d) for d in str(i))

        for i in range(1, n + 1):
            a = sum_of_digits(i)
            if a not in hash:
                hash[a] = 0
            hash[a] += 1

        max_val = max(hash.values())
        return sum(1 for v in hash.values() if v == max_val)
