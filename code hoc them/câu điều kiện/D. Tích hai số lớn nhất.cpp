#include <bits/stdc++.h>
using namespace std;
int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int p1 = a * b;
    int p2 = b * c;
    int p3 = a * c;

    int ans = max({p1, p2, p3});
    cout << ans;
    return 0;
}
