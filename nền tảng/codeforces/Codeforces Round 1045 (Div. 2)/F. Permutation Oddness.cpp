    #include <bits/stdc++.h>
    using namespace std;

    int lowbit(int x) {
        return x & (-x);
    }

    int main() {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int t;
        cin >> t;

        while (t--) {
            int c[4];
            cin >> c[0] >> c[1] >> c[2] >> c[3];

            int n = c[0] + c[1] + c[2] + c[3];
            vector<long long> result(2 * n, 0);

            function<void(vector<int>, int, int)> solve = [&](vector<int> remaining, int last, int sum) {
                if (accumulate(remaining.begin(), remaining.end(), 0) == 0) {
                    result[sum]++;
                    return;
                }

                for (int i = 0; i < 4; i++) {
                    if (remaining[i] > 0) {
                        remaining[i]--;
                        int new_sum = sum;
                        if (last != -1) {
                            new_sum += lowbit(last ^ i);
                        }
                        solve(remaining, i, new_sum);
                        remaining[i]++;
                    }
                }
            };

            vector<int> counts = {c[0], c[1], c[2], c[3]};
            solve(counts, -1, 0);

            // Output
            for (int i = 0; i < 2 * n; i++) {
                if (i > 0) cout << " ";
                cout << result[i];
            }
            cout << "\n";
        }

        return 0;
    }
