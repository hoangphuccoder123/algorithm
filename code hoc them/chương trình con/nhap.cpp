#include<bits/stdc++.h>

using namespace std;

#define int long long

int dem(int n){
    int ans = 0;
    while(n != 0){
    ans = ans * 10 + n % 10; // lấy chữ số cuối ghép vào kết quả
    n /= 10;
    }
    return ans;
}

bool 
int32_t main(){
     cout << dem(1234);
}
 