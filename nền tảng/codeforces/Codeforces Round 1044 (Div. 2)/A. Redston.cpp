#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        cin >> n;
        int freq[101] = {0};
        bool found = false;
        for (int i = 0; i < n; ++i) {
            int x; cin >> x;
            if (!found) {
                if (++freq[x] >= 2) found = true;
            }

        }
        cout << (found ? "YES\n" : "NO\n");
    }
    return 0;
} 