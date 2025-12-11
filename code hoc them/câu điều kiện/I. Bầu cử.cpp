#include<bits/stdc++.h>
#define int long long
using namespace std;
int a,b,c;
signed main(){
    cin>>a>>b>>c;
    int ans=max(a,b);
    int ans1= ans -c +1 ;
    cout<<ans1;
    return 0;
}
