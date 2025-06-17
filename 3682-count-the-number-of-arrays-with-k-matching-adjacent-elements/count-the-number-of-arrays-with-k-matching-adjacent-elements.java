class Solution {
    static final int MOD = 1_000_000_007;
    static long[] factorial = new long[100001]; // can be increased based on constraint
    static long[] inverseFactorial = new long[100001];
    static boolean precomputed = false;

    public int countGoodArrays(int n, int m, int k) {
        if (!precomputed) {
            precomputeFactorials(100000); // safe limit for constraints
        }

        long res = nCr(n - 1, k);
        res = (res * m) % MOD;
        res = (res * modPow(m - 1, n - k - 1)) % MOD;
        return (int) res;
    }

    private void precomputeFactorials(int limit) {
        factorial[0] = 1;
        for (int i = 1; i <= limit; i++) {
            factorial[i] = (factorial[i - 1] * i) % MOD;
        }

        inverseFactorial[limit] = modPow(factorial[limit], MOD - 2); // Fermat's Little Theorem
        for (int i = limit - 1; i >= 0; i--) {
            inverseFactorial[i] = (inverseFactorial[i + 1] * (i + 1)) % MOD;
        }

        precomputed = true;
    }

    private long nCr(int n, int r) {
        if (r < 0 || r > n) return 0;
        return factorial[n] * inverseFactorial[r] % MOD * inverseFactorial[n - r] % MOD;
    }

    private long modPow(long base, long exp) {
        long result = 1;
        base %= MOD;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }
}
