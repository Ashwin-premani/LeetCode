class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # if array is used then MLE and if linearly found TLE we need O(logn)

        def count_prefix(prefix: int) -> int:
            count = 0
            cur = prefix
            nex = prefix + 1
            while cur <= n:
                count += min(n + 1, nex) - cur
                cur *= 10
                nex *= 10
            return count

        curr = 1
        k -= 1  # Because we start at 1

        while k > 0:
            count = count_prefix(curr)
            if count <= k:
                curr += 1
                k -= count
            else:
                curr *= 10
                k -= 1

        return curr