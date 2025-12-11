# include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);                
    cin.tie(nullptr);

    int T; 
    if (!(cin >> T)) return 0;
    while (T--) {
        int r; cin >> r;
        if (r <= 1399) cout << "Division 4\n";
        else if (r <= 1599) cout << "Division 3\n";
        else if (r <= 1899) cout << "Division 2\n";
        else cout << "Division 1\n";
    }
    return 0;
}