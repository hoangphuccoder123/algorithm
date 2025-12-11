#include<iostream>
using namespace std;
int main(){
    int r;
    cin >> r;
    if (1 <= r && r <= 10) {
        cout << 10 << endl;
    } else if (11 <= r && r <= 20) {
        cout << 9 << endl;
    } else {
        cout << -1 << endl;
    }
    return 0;
} 