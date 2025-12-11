#include <bits/stdc++.h>
using namespace std;

// Hàm tính tổng bình phương từ 1 đến x
long long tongbinhphuong(long long x) {
    return x * (x + 1) * (2 * x + 1) / 6;
}

int main() {
    long long l, r;
    cin >> l >> r;

    long long ans = tongbinhphuong(r) - tongbinhphuong(l - 1);
    cout << ans << "\n";

    return 0;
}
