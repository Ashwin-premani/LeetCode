class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def primes(n):
            prime = [True] * (n+1)
            prime[0] = prime[1] = False
            for i in range(2, int(n*0.5) + 1):
                if prime[i]:
                    for j in range(i*i, n+1, i):
                        prime[j] = False
            return prime
        n = len(nums)
        max_val = max(max(row) for row in nums)
        prime = primes(max_val)
        max_prime = 0
        for i in range(n):
            if prime[nums[i][i]]:
                max_prime = max(max_prime, nums[i][i])
            if prime[nums[i][n - 1 - i]]:
                max_prime = max(max_prime, nums[i][n - 1 - i])
        return max_prime