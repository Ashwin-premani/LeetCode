#define MOD 1000000007
#define MAX_N 100005

long long factorial[MAX_N];
long long fermatFact[MAX_N];

// Binary exponentiation (iterative)
long long findPower(long long a, long long b) {
    long long result = 1;
    a %= MOD;
    while (b > 0) {
        if (b & 1) result = (result * a) % MOD;
        a = (a * a) % MOD;
        b >>= 1;
    }
    return result;
}

// nCr using Fermat's little theorem
long long nCr(int n, int r) {
    return factorial[n] * fermatFact[n - r] % MOD * fermatFact[r] % MOD;
}

int countGoodArrays(int n, int m, int k) {
    // Precompute factorials
    factorial[0] = factorial[1] = 1;
    for (int i = 2; i <= n; ++i) {
        factorial[i] = (factorial[i - 1] * i) % MOD;
    }

    // Precompute modular inverses using Fermat’s little theorem
    for (int i = 0; i <= n; ++i) {
        fermatFact[i] = findPower(factorial[i], MOD - 2);
    }

    long long result = nCr(n - 1, k);
    result = result * m % MOD;
    result = result * findPower(m - 1, n - k - 1) % MOD;

    return (int)result;
}
