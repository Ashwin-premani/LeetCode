class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = s.count('0')
        res = count
        power = 0
        val = 0

        for i in range(n-1, -1, -1):
            if s[i] == '1':
                if power < 32:
                    val += 1 << power
                    if val <= k:
                        res += 1
                    else:
                        break
                power += 1
            else:
                power += 1
        return res

        # MLE
        n = len(s)
        dp = [[-1] * (k + 2) for _ in range(n + 1)]
        
        def f(i, val):
            if i == n:
                return 0
            if val > k:
                return 0
            if dp[i][val] != -1:
                return dp[i][val]
            
            not_take = f(i + 1, val)
            
            new_val = val * 2 + int(s[i])
            take = 0
            if new_val <= k:
                take = 1 + f(i + 1, new_val)
            
            dp[i][val] = max(take, not_take)
            return dp[i][val]
        
        return f(0, 0)
        
       


        # TLE since we are using str
        n = len(s)
        def bin_dec(a):
            dec = 0
            power = len(a) - 1
            for bin in a:
                dec += int(bin) * (2**power)
                power -= 1
            return dec
        @lru_cache(None)
        def f(cur, i):
            if  i == n:
                return len(cur) if bin_dec(cur) <= k else 0
            not_take = f(cur, i+1)
            take = f(cur + s[i], i + 1)
            return max(take, not_take)
        return f("", 0)
        
        
        #TLE
        dp = {}
        def f(cur, i):
            if  i == n:
                return len(cur) if bin_dec(cur) <= k else 0
            if (i, cur) in dp:
                return dp[(i, cur)]
            not_take = f(cur, i+1)
            take = f(cur + s[i], i + 1)
            dp[(i, cur)] =  max(take, not_take)
            return dp[(i, cur)]
        return f("", 0)
            