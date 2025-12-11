#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        if (n <= 2) {
            for (int i = 1; i < n; ++i) {
                int u, v; cin >> u >> v;
            }
            cout << "-1\n";
            continue;
        }
        vector<vector<int>> g(n+1);
        for (int i = 1; i < n; ++i) {
            int u, v; cin >> u >> v;
            g[u].push_back(v);
            g[v].push_back(u);
        }

        // Check if already a path
        bool is_path = true;
        int b = -1;
        for (int i = 1; i <= n; ++i) {
            if (g[i].size() > 2) {
                is_path = false;
                b = i;
                break;
            }
        }

        if (is_path) {
            cout << "-1\n";
            continue;
        }

        // Find optimal a and c among neighbors of b
        vector<int> neighbors = g[b];
        int a = -1, c = -1;

        // Strategy: prefer leaves (degree 1) or nodes with smaller degrees
        // This helps minimize the total number of operations
        for (int neighbor : neighbors) {
            if (g[neighbor].size() == 1) {
                if (a == -1) a = neighbor;
                else if (c == -1) {
                    c = neighbor;
                    break;
                }
            }
        }

        // If we don't have two leaves, pick nodes with smallest degrees
        if (a == -1 || c == -1) {
            sort(neighbors.begin(), neighbors.end(), [&](int x, int y) {
                return g[x].size() < g[y].size();
            });
            a = neighbors[0];
            c = neighbors[1];
        }

        cout << a << " " << b << " " << c << "\n";
    }
    return 0;
}
