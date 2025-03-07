class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # sieve of eratosthenes
        def get_primes():
            is_prime = [True] * (right + 1)
            is_prime[0] = is_prime[1] = False

            for n in range(2, int(sqrt(right)) + 1):
                if not is_prime[n]:
                    continue
                for m in range(n+n, right + 1, n):
                    is_prime[m] = False
            primes = []
            for i in range(len(is_prime)):
                if is_prime[i] and i >= left:
                    primes.append(i)
            return primes

        primes = get_primes()
        res = [-1, -1]
        diff = right - left + 1
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < diff:
                diff = primes[i] - primes[i - 1]
                res = [primes[i - 1], primes[i]]
        return res
        # brute force
        # def isprime(n):
        #     if n < 2:
        #         return False
        #     if n == 2:
        #         return True
        #     if n % 2 == 0:
        #         return False
        #     for i in range(3, int(math.sqrt(n)) + 1, 2):
        #         if n % i == 0:
        #             return False
        #     return True
        
        # res = []
        # for i in range(left, right+1):
        #     if isprime(i):
        #         res.append(i)
        
        # n1 = -1
        # n2 = -1
        # m = float('inf')
        
        # for i in range(len(res) - 1):
        #     current_gap = res[i+1] - res[i]
        #     if current_gap < m:  # Changed from '>' to '<' and using strictly less than
        #         m = current_gap
        #         n1 = res[i]
        #         n2 = res[i+1]
        
        # return [n1, n2]