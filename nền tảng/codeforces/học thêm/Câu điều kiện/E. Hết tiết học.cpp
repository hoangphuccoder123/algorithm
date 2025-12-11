#include <iostream>
using namespace std;

int main() {
    int k;
    if (!(cin >> k)) return 0;
    int total = 7 * 60; 
    for (int i = 1; i <= k; ++i) {
        total += 45;
        if (i == k) break;
        if (i == 1 || i == 3) total += 10;  
        else total += 5;                    
    }
    cout << (total / 60) << ' ' << (total % 60) << '\n';
    return 0;
}