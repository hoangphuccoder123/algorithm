#include <iostream>
using namespace std;
int main() {
    long long a,b,c;
    if (!(cin >> a >> b >> c)) return 0;
    if (a == b || a == c) cout << a << '\n';
    else if (b == c) cout << b << '\n';
    else cout << -1 << '\n';
    return 0;
} 