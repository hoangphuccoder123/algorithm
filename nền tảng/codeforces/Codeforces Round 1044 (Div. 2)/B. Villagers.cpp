#include <iostream>
#include <vector>
#include <numeric>

void solve() {
    int n;
    std::cin >> n;
    long long total_grumpiness = 0;
    for (int i = 0; i < n; ++i) {
        long long g;
        std::cin >> g;
        total_grumpiness += g;
    }

    // The minimum total emeralds required to make everyone friends
    // is equal to the initial total grumpiness of the village.
    std::cout << total_grumpiness << "\n";
}

int main() {
    // Fast I/O
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}