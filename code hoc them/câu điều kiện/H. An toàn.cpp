#include<bits/stdc++.h>
using namespace std;
int a,b,c;
#define int long long
signed  main(){
    cin>>a>>b>>c;
    int ans= a+b+c -max(a,max(b,c))-min(a,min(b,c));
    cout<<ans;

}
