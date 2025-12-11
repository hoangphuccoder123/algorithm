#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int soBoTest; 
	if (!(cin >> soBoTest)) return 0;
	while (soBoTest--) {
		int n; cin >> n;
		vector<long long> w(n);
		for (int i = 0; i < n; ++i) cin >> w[i];

		int l = 0, r = n - 1; // Alice ăn từ trái, Bob ăn từ phải
		long long sumL = 0, sumR = 0;
		int kq = 0; // số kẹo tối đa (đếm theo số viên)

		while (l <= r) {
			if (sumL <= sumR) {
				sumL += w[l++];
			} else {
				sumR += w[r--];
			}
			if (sumL == sumR) {
				// tổng bằng nhau -> cập nhật số viên đã ăn
				kq = max(kq, l + (n - 1 - r));
			}
		}
		cout << kq << '\n';
	}
	return 0;
}

