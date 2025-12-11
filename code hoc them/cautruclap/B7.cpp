#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; cin >> n;
    unsigned long long fact = 1;
    for (int i = 2; i <= n; i++) fact *= i;
    cout << fact << "\n";
    return 0;
}
