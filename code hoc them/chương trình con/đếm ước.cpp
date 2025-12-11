#include<bits/stdc++.h>

using namespace std;

#define int long long

int demUoc(int n){
    if(n <= 0) return 0;
    int ans= 0;
    for(int i = 1; i * i <= n; ++i){
        if(n % i == 0){
            if(i * i == n) ans+= 1; 
            else ans+= 2;           
        }
    }
    return ans ;
} 
int32_t main(){
    int n;
    cin >> n;
    if(cp(n)){
        cout << "Yes";
    }
    else
      cout << "No";
} 