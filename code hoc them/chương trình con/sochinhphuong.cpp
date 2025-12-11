#include<bits/stdc++.h>

using namespace std;

#define int long long

bool cp(int n){
     int x = sqrt(n);
     if(x * x == n)
      return true;
     else
      return false;
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