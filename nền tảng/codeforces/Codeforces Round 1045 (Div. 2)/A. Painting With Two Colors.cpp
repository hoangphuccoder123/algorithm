    #include <bits/stdc++.h>
    using namespace std;

    int main() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);

        int t;
        if (!(cin >> t)) return 0;
        while (t--) {
            long long n, a, b;
            cin >> n >> a >> b;
            bool ok = false;
            if (((n - b) & 1LL) == 0) {
                if (a <= b) ok = true;
                else if (((n - a) & 1LL) == 0) ok = true;
            }
            cout << (ok ? "YES" : "NO") << '\n';
        }
        return 0;
    }
