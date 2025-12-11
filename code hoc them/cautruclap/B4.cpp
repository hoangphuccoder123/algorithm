#include<bits/stdc++.h>
#define int long long
using namespace std;
int l,r;
bool sum(long long x){
    return x*(x+1)/2;
}
signed main(){
    cin>>l>>r;
    int ans = sum(r)-sum(l-1);
    cout<<ans;
}
