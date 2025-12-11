#include<bits/stdc++.h>

using namespace std;

#define int long long

int dem(int n){
    int ans = 0;
    while(n != 0){
      ans += n % 10;
      n /= 10;
    }
    return ans;
}

int32_t main(){


     cout << dem(1234);
}
