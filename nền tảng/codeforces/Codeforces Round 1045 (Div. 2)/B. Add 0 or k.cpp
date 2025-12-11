#include <bits/stdc++.h>
using namespace std;

// Constructive solution:
// Pick a small prime p that does NOT divide k and p <= k+1.
// For each ai, choose si in [0, p-1] such that ai + si*k == 0 (mod p).
// Since gcd(k, p) = 1, si = (-ai) * inv(k) mod p exists and si <= p-1 <= k.
// Then all numbers are multiples of p, so gcd > 1.

static const int SMALL_PRIMES[] = {
    2,3,5,7,11,13,17,19,23,29,31,37,41,43
};

long long mod_pow(long long a, long long e, long long mod) {
    long long r = 1 % mod;
    a %= mod;
    while (e) {
        if (e & 1) r = (__int128)r * a % mod;
        a = (__int128)a * a % mod;
        e >>= 1;
    }
    return r;
}

int pick_prime(long long k) {
    for (int p : SMALL_PRIMES) {
        if (p > k + 1) break; // must satisfy p <= k+1
        if (k % p != 0) return p;
    }
    // Fallback (should never happen for k <= 1e9): search upwards for a prime <= k+1 not dividing k
    long long limit = k + 1;
    auto isPrime = [](long long x){
        if (x < 2) return false;
        for (long long d = 2; d * d <= x; ++d) if (x % d == 0) return false;
        return true;
    };
    for (long long p = 47; p <= limit; ++p) {
        if (isPrime(p) && k % p != 0) return (int)p;
    }
    // As a last resort (theoretical), if all primes <= k+1 divide k, then pick p=2 and k must be 1 -> ok
    return 2;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n; long long k;
        cin >> n >> k;
        vector<long long> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];

        int p = pick_prime(k);
        // modular inverse of k modulo p (p is prime and gcd(k,p)=1)
        long long invk = mod_pow((k % p + p) % p, p - 2, p);

        for (int i = 0; i < n; ++i) {
            long long r = (a[i] % p + p) % p; // ai mod p
            long long si = (p - r) % p;       // target: r + si*(k%p) == 0 mod p -> si == (-r) * invk
            si = (si * invk) % p;
            // si in [0, p-1] <= k because p <= k+1
            a[i] += si * k;
        }

        for (int i = 0; i < n; ++i) {
            if (i) cout << ' ';
            cout << a[i];
        }
        cout << '\n';
    }
    return 0;
}

