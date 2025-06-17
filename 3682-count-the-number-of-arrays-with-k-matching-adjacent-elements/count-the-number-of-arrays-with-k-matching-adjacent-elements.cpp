#include <vector>
using namespace std;

class Solution {
    const int MOD = 1e9 + 7;

    // Iterative Binary Exponentiation
    long long findPower(long long base, long long exp) {
        long long result = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp & 1) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }

    // Compute nCr using Fermat's little theorem
    long long nCr(int n, int r, const vector<long long>& factorial, const vector<long long>& fermatFact) {
        return factorial[n] * fermatFact[n - r] % MOD * fermatFact[r] % MOD;
    }

public:
    int countGoodArrays(int n, int m, int k) {
        vector<long long> factorial(n + 1, 1);
        for (int i = 2; i <= n; ++i) {
            factorial[i] = (factorial[i - 1] * i) % MOD;
        }

        vector<long long> fermatFact(n + 1, 1);
        for (int i = 0; i <= n; ++i) {
            fermatFact[i] = findPower(factorial[i], MOD - 2); // Fermat inverse
        }

        long long result = nCr(n - 1, k, factorial, fermatFact);
        result = result * m % MOD;
        result = result * findPower(m - 1, n - k - 1) % MOD;
        return result;
    }
};
