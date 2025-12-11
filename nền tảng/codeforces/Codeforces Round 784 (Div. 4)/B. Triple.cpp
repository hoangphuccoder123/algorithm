#include<bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        cin >> n;
        vector<int> freq(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            int x; cin >> x;
            if (1 <= x && x <= n) ++freq[x];
        }
        int ans = -1;
        for (int v = 1; v <= n; ++v) {
            if (freq[v] >= 3) ans = v; // không break: lấy giá trị lớn nhất thỏa điều kiện
        }
        cout << ans << '\n';
    }
    return 0;
}