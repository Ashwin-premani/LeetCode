class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # using string
        n = len(str1)
        m = len(str2)
        
        # Build LCS DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Reconstruct SCS using string only
        i, j = n, m
        result = ""
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result = str1[i - 1] + result
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result = str1[i - 1] + result
                i -= 1
            else:
                result = str2[j - 1] + result
                j -= 1
        
        # Add remaining characters
        while i > 0:
            result = str1[i - 1] + result
            i -= 1
        while j > 0:
            result = str2[j - 1] + result
            j -= 1
        
        return result

        # using array
        n = len(str1)
        m = len(str2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        i, j = n, m
        result = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(str1[i - 1])
                i -= 1
            else:
                result.append(str2[j - 1])
                j -= 1
        
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        
        result.reverse()
        return ''.join(result)



        n, m = len(str1), len(str2)

        prev = [str2[j:] for j in range(m)]
        prev.append("")
        for i in reversed(range(n)):
            cur = [""] * m
            cur.append(str1[i:])
            for j in reversed(range(m)):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + prev[j+1]
                else:
                    res1 = str1[i] + prev[j]
                    res2 = str2[j] + cur[j+1]
                    if len(res1) < len(res2):
                        cur[j] = res1
                    else:
                        cur[j] = res2
            prev = cur
        return cur[0]


        # cache = {}
        # def backtrack(i, j):
        #     if (i, j) in cache:
        #         return cache[(i,j)]
        #     if i ==len(str1):
        #         return str2[j:]
        #     if j == len(str2):
        #         return str1[i:]
            
        #     if str1[i] == str2[j]:
        #         return str1[i] + backtrack(i+1, j+1)
            
        #     res1 = str1[i] + backtrack(i+1, j)
        #     res2 = str2[j] + backtrack(i, j+1)
        #     if len(res1) > len(res2):
        #         cache[(i,j)] = res2
        #         return res2
        #     cache[(i,j)] = res1
        #     return res1
        # return backtrack(0,0)