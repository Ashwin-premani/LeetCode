class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        max_len = n // k

        # Step 1: Count characters that appear at least k times
        count = Counter(s)
        count = {char: count[char] // k for char in count if count[char] >= k}
        chars = sorted(count.keys())  # sort for lex order

        subseq = []

        # Step 2: Generate all subsequences using allowed frequencies
        def backtrack(path, used_count):
            if len(path) > max_len:
                return
            if path:
                subseq.append(''.join(path))
            for ch in chars:
                if used_count[ch] < count[ch]:
                    used_count[ch] += 1
                    path.append(ch)
                    backtrack(path, used_count)
                    path.pop()
                    used_count[ch] -= 1

        backtrack([], Counter())
        subseq.sort(key=lambda x: (len(x), x), reverse=True)
        for i in subseq:
            a = i * k
            m = 0
            for j in range(len(s)):
                if s[j] == a[m]:
                    m += 1
                    if m == len(a):
                        return i

        return ""
