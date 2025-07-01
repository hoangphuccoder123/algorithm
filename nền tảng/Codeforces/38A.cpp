#include <bits/stdc++.h> 
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n; cin >> n;
    int d[n]; // Mảng lưu khoảng cách giữa các cấp bậc
    for(int i = 1; i < n; i++){
        cin >> d[i]; 
    }
    
    int a, b; cin >> a >> b;
    int sum = 0;
    for(int i = a; i < b; i++){
        sum += d[i];
    }
    cout << sum;
    
    return 0;
}