#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 4e18; // Sử dụng một giá trị vô cùng lớn

void solve() {
    int n;
    cin >> n;
    vector<long long> h(n);
    for (int i = 0; i < n; ++i) {
        cin >> h[i];
    }

    if (n == 0) {
        cout << 0 << endl;
        return;
    }

    // dp[i][0]: chi phí tối thiểu để dọn sạch i mob đầu tiên, mob thứ i bị giết bằng đòn tấn công trực tiếp.
    // dp[i][1]: chi phí tối thiểu để dọn sạch i mob đầu tiên, mob thứ i bị giết bởi sát thương rơi từ mob i-1.
    vector<vector<long long>> dp(n + 1, vector<long long>(2, INF));

    // Khởi tạo cho trường hợp cơ sở
    dp[0][0] = 0;

    // Tính toán cho mob đầu tiên (i=1)
    dp[1][0] = h[0];

    // Vòng lặp quy hoạch động
    for (int i = 2; i <= n; ++i) {
        // Tính dp[i][0]: mob i (h[i-1]) bị giết bằng đòn tấn công trực tiếp.
        // Điều này có thể xảy ra sau khi dọn sạch i-1 mob đầu tiên.
        // Mob i-1 có thể bị giết bằng tấn công (dp[i-1][0]) hoặc sát thương rơi (dp[i-1][1]).
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + h[i - 1];

        // Tính dp[i][1]: mob i (h[i-1]) bị giết bởi sát thương rơi từ mob i-1 (h[i-2]).
        // Điều này yêu cầu chúng ta phải tấn công mob i-1.
        // Trạng thái trước đó là i-2 mob đầu tiên đã được dọn sạch.
        // Mob i-2 có thể bị giết bằng tấn công (dp[i-2][0]) hoặc sát thương rơi (dp[i-2][1]).
        long long cost_to_kill_i_minus_1 = h[i - 2];
        dp[i][1] = min(dp[i - 2][0], dp[i - 2][1]) + cost_to_kill_i_minus_1;
    }

    // Kết quả cuối cùng là chi phí tối thiểu để dọn sạch tất cả n mob.
    cout << min(dp[n][0], dp[n][1]) << endl;
}

int main() {
    // Tăng tốc độ nhập xuất
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}