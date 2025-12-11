#include<bits/stdc++.h>
#define int long long
int n;
using namespace std;
bool sochinhphuong(int n){
    if (n<0) return false;
    int k=sqrt(n);
    return k*k=n;
}
signed main(){
    cin>>n;
    if (sochinhphuong(n)){
        cout<<"YES"
    }else{
        return"NO"
    }
    return 0;
}
