#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, M;
    cin >> n >> M;

    vector<int> dp(M + 1, 0); // Mảng lưu giá trị lớn nhất với trọng lượng tối đa từ 0 đến M

    for (int i = 0; i < n; ++i) {
        int weight, value;
        cin >> weight >> value;
        // Duyệt ngược để tránh ghi đè giá trị trong cùng vòng lặp
        for (int j = M; j >= weight; --j) {
            dp[j] = max(dp[j], dp[j - weight] + value);
        }
    }

    cout << dp[M] << endl; // Giá trị lớn nhất có thể đạt được

    return 0;
}
