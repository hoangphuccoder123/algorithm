#include<bits/stdc++.h>
#define int long long
using namespace std;
int a,b,c;
signed main(){
    cin>>a>>b>>c;
    int ans = a+b+c -min(a,min(b,c))-max(a,max(b,c));
    cout<<ans;
}
