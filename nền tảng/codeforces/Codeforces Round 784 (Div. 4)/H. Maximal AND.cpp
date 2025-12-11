#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int soBoTest; 
    if (!(cin >> soBoTest)) return 0;
    while (soBoTest--) {
        int n; long long k; 
        cin >> n >> k;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];

        long long ans = 0;
        // Duyệt bit từ cao xuống thấp; nếu có thể bật bit j cho tất cả phần tử với <= k thao tác thì bật
        for (int j = 30; j >= 0; --j) {
            int dem0 = 0;
            for (int x : a) if (((x >> j) & 1) == 0) ++dem0;
            if (dem0 <= k) {
                k -= dem0;
                ans |= (1LL << j);
            }
        }
        cout << ans << '\n';
    }
    return 0;
}
