#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int soBoTest; 
	if (!(cin >> soBoTest)) return 0;
	while (soBoTest--) {
		int n, m; 
		cin >> n >> m;
		vector<string> a(n);
		for (int i = 0; i < n; ++i) cin >> a[i];

		// Xử lý từng cột độc lập: đi từ dưới lên, gom các viên '*' rơi xuống trong đoạn không có 'o'
		for (int c = 0; c < m; ++c) {
			int day = n - 1; // vị trí thấp nhất hiện tại nơi viên đá sẽ rơi tới (trước chướng ngại)
			for (int r = n - 1; r >= 0; --r) {
				if (a[r][c] == 'o') { // chướng ngại: đặt lại đáy cho đoạn phía trên
					day = r - 1;
				} else if (a[r][c] == '*') {
					// cho viên đá này rơi tới "day"
					a[r][c] = '.';
					a[day][c] = '*';
					--day;
				}
				// nếu là '.', bỏ qua
			}
		}

		for (int i = 0; i < n; ++i) cout << a[i] << '\n';
	}
	return 0;
}

