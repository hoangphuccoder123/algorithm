#include<bits/stdc++.h>
#define int long long
int a,b,c,d;
using namespace std;
signed main(){
    cin>>a>>b>>c>>d;
    int ans=max(a,b);
    int ans1=max(c,d);
    int ans2=max(ans,ans1);
    cout<<ans2;
}
