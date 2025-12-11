#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
    int n;
    cin >> n;
    for (int i = n; i >= 1; --i) {
        cout << i;
        if (i != 1) cout << " "; // chỉ in khoảng trắng nếu chưa đến số cuối
    }
    cout << "\n";
    return 0;
}

