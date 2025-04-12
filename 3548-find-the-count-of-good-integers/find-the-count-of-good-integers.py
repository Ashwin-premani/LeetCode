class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dictionary = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1
        # Enumerate the number of palindrome numbers of n digits
        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            palindromicInteger = int(s)
            # If the current palindrome number is a k-palindromic integer
            if palindromicInteger % k == 0:
                sorted_s = "".join(sorted(s))
                dictionary.add(sorted_s)

        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dictionary:
            cnt = [0] * 10
            for c in s:
                cnt[int(c)] += 1
            # Calculate permutations and combinations
            tot = (n - cnt[0]) * fac[n - 1]
            for x in cnt:
                tot //= fac[x]
            ans += tot

        return ans


        def generate_k_palindromes(n, k):
            palindromes = []
            if n == 1:
                for i in range(1, 10):
                    if i % k == 0:
                        palindromes.append(str(i))
            elif n % 2 == 0:
                half = n // 2
                for i in range(10 ** (half - 1), 10 ** half):
                    s = str(i)
                    p = s + s[::-1]
                    if int(p) % k == 0:
                        palindromes.append(p)
            else:
                half = n // 2
                for i in range(10 ** (half - 1), 10 ** half):
                    s = str(i)
                    for m in range(10):
                        p = s + str(m) + s[::-1]
                        if int(p) % k == 0:
                            palindromes.append(p)
            return palindromes

        # Step 1: generate palindromic digit count signatures
        palins = generate_k_palindromes(n, k)
        pset = set()
        for p in palins:
            pset.add(tuple(sorted(Counter(p).items())))

        # Step 2: iterate through all n-digit numbers
        res = 0
        low = 10 ** (n - 1)
        high = 10 ** n
        for i in range(low, high):
            c = Counter(str(i))
            if tuple(sorted(c.items())) in pset:
                res += 1

        return res






        # TLE but optimized with set
        def generate_k_palindromes(n, k):
            palindromes = set()
            if n == 1:
                for i in range(1, 10):
                    if i % k == 0:
                        palindromes.add(''.join(sorted(str(i))))
            elif n % 2 == 0:
                half = n // 2
                for i in range(10 ** (half - 1), 10 ** half):
                    s = str(i)
                    num = int(s + s[::-1])
                    if num % k == 0:
                        palindromes.add(''.join(sorted(str(num))))
            else:
                half = n // 2
                for i in range(10 ** (half - 1), 10 ** half):
                    s = str(i)
                    for mid in range(10):
                        num = int(s + str(mid) + s[::-1])
                        if num % k == 0:
                            palindromes.add(''.join(sorted(str(num))))
            return palindromes

        valid_signatures = generate_k_palindromes(n, k)
        count = 0
        for num in range(10 ** (n - 1), 10 ** n):
            if ''.join(sorted(str(num))) in valid_signatures:
                count += 1
        return count



        # TLE
        # def generate_k_palindromes(n, k):
        #     palindromes = []
        #     if n == 1:
        #         for i in range(1, 10):
        #             if i % k == 0:
        #                 palindromes.append(i)
        #     elif n % 2 == 0:
        #         half_length = n // 2
        #         start = 10**(half_length - 1)
        #         end = 10**half_length
        #         for i in range(start, end):
        #             s = str(i)
        #             num = int(s + s[::-1])
        #             if num % k == 0:
        #                 palindromes.append(num)
        #     else:
        #         half_length = n // 2
        #         start = 10**(half_length - 1)
        #         end = 10**half_length
        #         for i in range(start, end):
        #             s = str(i)
        #             for j in range(10):
        #                 num = int(s + str(j) + s[::-1])
        #                 if num % k == 0:
        #                     palindromes.append(num)
        #     return palindromes
        
        # def find_good_integers(n: int, palindromes: List[int]) -> int:
        #     count = 0
        #     palin_maps = [Counter(str(p)) for p in palindromes]
        #     start = 10**(n-1)
        #     end = 10**n

        #     for num in range(start, end):
        #         num_counter = Counter(str(num))
        #         for pal_counter in palin_maps:
        #             if num_counter == pal_counter:
        #                 count += 1
        #                 break
        #     return count

        # k_palindromes = generate_k_palindromes(n, k)
        # return find_good_integers(n, k_palindromes)
