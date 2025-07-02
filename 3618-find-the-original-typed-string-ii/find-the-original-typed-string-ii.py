class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(word)
        count = 1
        freq = []

        for i in range(1, n):
            if word[i] == word[i - 1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)

        P = 1
        for f in freq:
            P = (P * f) % MOD

        if len(freq) >= k:
            return P

        prev = [1] + [0] * (k - 1)
        prefix = [1] * k

        for i in range(len(freq)):
            cur = [0] * k
            for j in range(1, k):
                cur[j] = prefix[j - 1]
                if j - freq[i] - 1 >= 0:
                    cur[j] = (cur[j] - prefix[j - freq[i] - 1]) % MOD
            new_prefix = [cur[0]] + [0] * (k - 1)
            for j in range(1, k):
                new_prefix[j] = (new_prefix[j - 1] + cur[j]) % MOD
            prev, prefix = cur, new_prefix

        return (P - prefix[k - 1]) % MOD


        

        # recursion + memoization -> MLE
        MOD = 10**9 + 7
        freq = []
        n = len(word)
        count = 1
        for i in range(1, n):
            if word[i] == word[i-1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)

        @lru_cache(maxsize=None)
        def solve(i, count):
            if i >= len(freq):
                if count < k:
                    return 1
                else:
                    return 0
            
            res = 0
            for take in range(1, freq[i] + 1):
                if take + count < k:
                    res = (res + solve(i+1, count + take)) % MOD
                else:
                    break
            return res % MOD
        
        C = solve(0, 0)
        P = 1
        for i in freq:
            P *= i
        return (P - C) % MOD