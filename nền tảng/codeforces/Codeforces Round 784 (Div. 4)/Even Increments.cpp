#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Đổi tên biến sang tiếng Việt cho dễ hiểu
    int soBoTest; 
    if (!(cin >> soBoTest)) return 0;
    while (soBoTest--) {
        int soPhanTu; 
        cin >> soPhanTu;
        // mauLe: parity tham chiếu cho các vị trí lẻ; mauChan: cho các vị trí chẵn
        int mauLe = -1, mauChan = -1; 
        bool hopLe = true;
        for (int viTri = 1; viTri <= soPhanTu; ++viTri) {
            int giaTri; cin >> giaTri;
            int chanLe = giaTri & 1;
            if (viTri & 1) {
                if (mauLe == -1) mauLe = chanLe;
                else if (mauLe != chanLe) hopLe = false;
            } else {
                if (mauChan == -1) mauChan = chanLe;
                else if (mauChan != chanLe) hopLe = false;
            }
        }
        cout << (hopLe ? "YES" : "NO") << '\n';
    }
    return 0;
}
