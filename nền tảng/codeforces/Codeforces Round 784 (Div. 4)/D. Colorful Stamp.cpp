#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int soBoTest; 
    if (!(cin >> soBoTest)) return 0;
    while (soBoTest--) {
        int n; string s;
        cin >> n >> s;

        bool hopLe = true;
        for (int i = 0; i < n; ) {
            if (s[i] == 'W') { ++i; continue; }
            // Xét một đoạn liên tiếp không có 'W'
            bool coR = false, coB = false;
            int j = i;
            while (j < n && s[j] != 'W') {
                coR |= (s[j] == 'R');
                coB |= (s[j] == 'B');
                ++j;
            }
            if (!(coR && coB)) { // đoạn chỉ gồm 1 màu -> không thể đóng dấu để ra được
                hopLe = false;
                break;
            }
            i = j; // nhảy sang sau đoạn này
        }
        cout << (hopLe ? "YES" : "NO") << '\n';
    }
    return 0;
}
