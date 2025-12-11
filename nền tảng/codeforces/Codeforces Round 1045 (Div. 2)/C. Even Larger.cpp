
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n; cin >> n;
        vector<long long> a(n+1);
        for (int i = 1; i <= n; ++i) cin >> a[i];

        // b[i] = +a[i] if i is even, else -a[i]
        vector<long long> pref(n+1, 0); // S[0]=0
        for (int i = 1; i <= n; ++i) {
            long long bi = (i % 2 == 0) ? a[i] : -a[i];
            pref[i] = pref[i-1] + bi;
        }

        vector<long long> T(n+1, 0), Pmax(n+1, 0);
        T[0] = 0; Pmax[0] = 0;

        long long ycum = 0; // total decrements applied to odd indices up to current latest odd
        long long ops = 0;  // total operations

        for (int k = 1; k <= n; ++k) {
            long long threshold = LLONG_MIN;
            if (k >= 2) threshold = Pmax[k-2];
            long long baseline = pref[k] + ycum;
            if (k >= 2 && baseline < threshold) {
                long long deficit = threshold - baseline;
                // allocate at latest odd <= k
                int p = (k % 2 == 1) ? k : (k-1);
                // No need to explicitly track per-index capacity since we can always distribute
                // across odd indices; allocating at the latest odd gives minimal future impact.
                // We just add to ycum.
                ycum += deficit;
                ops += deficit;
                baseline += deficit;
            }
            T[k] = baseline;
            Pmax[k] = max(Pmax[k-1], T[k]);
        }

        cout << ops << "\n";
    }
    return 0;
}

