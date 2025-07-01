#include <bits/stdc++.h> 
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t; 
    while(t--){
        char a ,b,c,d,e,f ;cin >> a >> b >> c >> d >> e >> f; 
        if ((a-'0') + (b-'0') + (c-'0') == (d-'0') + (e-'0') + (f-'0')) cout << "YES\n"; 
        else cout << "NO\n";
    }
    return 0;
}