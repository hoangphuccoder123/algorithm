#include<bits/stdc++.h>
#define int long long
using namespace std;
int n,m;
signed main(){
    cin>>n>>m;
    for (int i=0 ; i>=m ; i++){
        cout<<n*i;
        if(i<m) cout<<"";
    }
    return 0;
}
