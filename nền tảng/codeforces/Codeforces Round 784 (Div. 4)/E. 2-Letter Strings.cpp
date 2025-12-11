#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int soBoTest; 
    if (!(cin >> soBoTest)) return 0;
    while (soBoTest--) {
        int soChuoi; cin >> soChuoi;
        long long kq = 0;
        long long demDau[26] = {0};
        long long demCuoi[26] = {0};
        long long demCap[26][26];
        memset(demCap, 0, sizeof(demCap));

        for (int i = 0; i < soChuoi; ++i) {
            string s; cin >> s; // độ dài đúng 2
            int a = s[0] - 'a';
            int b = s[1] - 'a';
            // Cộng số cặp trước đó khác đúng 1 vị trí
            kq += demDau[a] + demCuoi[b] - 2LL * demCap[a][b];
            // Cập nhật tần suất
            ++demDau[a];
            ++demCuoi[b];
            ++demCap[a][b];
        }
        cout << kq << '\n';
    }
    return 0;
}
