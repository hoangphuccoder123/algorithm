#include <bits/stdc++.h>
#define int long long
using namespace std;

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {   // nhập từ 0 đến n-1
        cin >> a[i];
    }

    // giả sử n >= 2
    int max_qua = a[0] + a[1];       // tổng 2 phần tử liên tiếp đầu tiên

    for (int i = 1; i < n - 1; ++i) { // duyệt đến phần tử áp chót
        max_qua = max(max_qua, a[i] + a[i + 1]);
    }

    cout << max_qua << '\n';
    return 0;
}
