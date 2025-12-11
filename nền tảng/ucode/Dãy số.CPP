#include<bits/stdc++.h>
#define int long long 
#pragma GCC optimize("O3")
using namespace std;
int n;
bool snt(int n ){
    if(n<2) return false;
    for(int i=2;i*i<=n;++i){
        if(n%i==0) return false;
    }
    return true; 
}
signed main(){
    cin>>n;
    vector<int>a(n+1);
    for(int i=1;i<=n;i++){
        cin>>a[i];
    }
    // Tìm số nguyên tố lớn nhất trong mảng
    int max_snt = -1;  // Khởi tạo -1 nếu không có
    for(int i=1;i<=n;i++){
        if(snt(a[i]) && a[i] > max_snt){
            max_snt = a[i];
        }
    }
    // ko có snt 
    if (max_snt == -1) max_snt = 0;
    map<int, int> freq;      // đếm tần suất
    for (int i = 1; i <= n; i++) {
        freq[a[i]]++;
    }
    cout << max_snt << "\n" << cnt;
    return 0;
} 
