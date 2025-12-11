#include<bits/stdc++.h>

using namespace std;

#define int long long

const int N = 1e6 + 5;
int n;
int a[N];

int32_t main(){
     cin >> n;
     for(int i = 1 ;i <= n ; i++){
          cin >> a[i];
          if (a[i]<0){
            a[i]=-a[i];
          }
     }
     for(int i = 1 ; i <= n ; i++){  
         cout << a[i] << " ";
    }
    return 0;
} 