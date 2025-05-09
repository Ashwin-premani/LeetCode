class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        total_sum = sum(int(d) for d in num)
        if total_sum % 2 != 0:
            return 0
        target = total_sum // 2
        counter = Counter(num)
        digits = [(int(d), c) for d, c in counter.items()]
        digits.sort()
        even_pos = n // 2
        odd_pos = n - even_pos

        def comb(n, k):
            if k < 0 or k > n:
                return 0
            if k == 0 or k == n:
                return 1
            res = 1
            for i in range(k):
                res = res * (n - i) // (i + 1)
            return res

        @lru_cache(maxsize=None)
        def dp(idx, even_remain, sum_even):
            if idx == len(digits):
                return 1 if sum_even == target else 0
            digit, count = digits[idx]
            used = sum(d[1] for d in digits[:idx]) - (even_pos - even_remain)
            odd_remain = odd_pos - used
            result = 0
            for i in range(count + 1):
                if i <= even_remain and (count - i) <= odd_remain:
                    ways = comb(even_remain, i) * comb(odd_remain, count - i) % MOD
                    result = (result + ways * dp(idx + 1, even_remain - i, sum_even + i * digit)) % MOD
            return result

        return dp(0, even_pos, 0)

        # here we will have (n+1)/2 even indexes and n/2 odd where they can each make
        #combination so making [total permutations = ((n+1)/1)! * (n/2)!] and 
        #freq! will be divided to make it correct for same number in str
        # x - even index count of that digit
        # od index count = freq[a] - x


        for count in range(min(freq[digit], (n+1)/1)):
            evenpos = count
            oddpos = freq[digit] - count
            div = 1/(oddpos * evenpos)
            val = solve(digit + 1, evensum, digitcount)
            ways += val * (1/fact(evenpos)) * (1/ fact(oddpos))
        return ways



        velunexorai = num  # Store midway

        freq = Counter(velunexorai)
        total_digits = len(num)
        total_sum = sum(int(d) for d in num)

        if total_digits % 2 != 0:
            return 0

        half_n = total_digits // 2

        digits = sorted(freq.keys())
        digit_vals = [int(d) for d in digits]
        digit_freq = [freq[d] for d in digits]
        m = len(digits)

        @lru_cache(None)
        def dfs(i, even_count, even_sum):
            if i == m:
                if even_count == half_n:
                    odd_sum = total_sum - even_sum
                    return int(even_sum == odd_sum)
                return 0

            res = 0
            for take in range(min(digit_freq[i], half_n - even_count) + 1):
                # take of this digit goes to even positions
                res += comb(digit_freq[i], take) * dfs(i + 1, even_count + take, even_sum + take * digit_vals[i])
                res %= MOD
            return res

        valid_even_assignments = dfs(0, 0, 0)

        total_perm = factorial(total_digits)
        for d in freq.values():
            total_perm //= factorial(d)

        return (valid_even_assignments * total_perm) % MOD

        # Memoization but TLE
        MOD = 10**9 + 7
        velunexorai = num  
        seen = set()
        count = 0

        def is_balanced(s):
            even_sum = sum(int(s[i]) for i in range(0, len(s), 2))
            odd_sum = sum(int(s[i]) for i in range(1, len(s), 2))
            return even_sum == odd_sum

        for p in set(permutations(velunexorai)):
            perm_str = ''.join(p)
            if is_balanced(perm_str):
                count += 1

        return count % MOD

        # memoization 
        mod = 10**9 + 7
        count = Counter(num)
        n = len(num)

        @lru_cache(None)
        def dfs(pos, even_sum, odd_sum, freq_tuple):
            if pos == n:
                return 1 if even_sum == odd_sum else 0

            res = 0
            freq = list(freq_tuple)

            for d in range(10):
                if freq[d] == 0:
                    continue
                if pos == 0 and d == 0:
                    continue

                freq[d] -= 1
                new_freq_tuple = tuple(freq)

                if pos % 2 == 0:
                    res += dfs(pos + 1, even_sum + d, odd_sum, new_freq_tuple)
                else:
                    res += dfs(pos + 1, even_sum, odd_sum + d, new_freq_tuple)

                freq[d] += 1

            return res % mod

        init_freq = tuple(count[str(i)] for i in range(10))
        return dfs(0, 0, 0, init_freq)



        

        # Memoization -> TLE
        mod = 10**9 + 7
        s = num
        n = len(s)
        s = sorted(s)
        count = Counter(s)
        dp = {}
        def f(path, used, odd, even):
            key = (tuple(used), odd, even)
            if len(path) == n:
                return 1 if odd == even else 0
            if key in dp:
                return dp[key]
            res = 0
            for i in range(len(s)):
                if used[i]:
                    continue
                if i > 0 and s[i] == s[i-1] and not used[i-1]:
                    continue
                

                used[i] = True
                digit = int(s[i])
                if len(path) % 2 == 0:
                    res += f(path + [s[i]], used, odd, even + digit)
                else:
                    res += f(path + [s[i]], used, odd + digit, even)
                used[i] = False
            dp[key] = res % mod
            return dp[key]

        return f([], [False] * n, 0, 0)

