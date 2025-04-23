class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict

        count = defaultdict(int)
        max_size = 0 

        def sum_of_digits(x):
            return sum(int(d) for d in str(x))

        for i in range(1, n + 1):
            s = sum_of_digits(i)
            count[s] += 1
            max_size = max(max_size, count[s])

        return sum(1 for v in count.values() if v == max_size)



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
