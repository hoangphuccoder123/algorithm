#include<bits/stdc++.h>
#define int long long
using namespace std;
int n,m;
signed main(){
    cin>>n>>m;
    for(int i =1 ; i<=n;i++){
        for(int j=1 ;j<=m;j++){
            cout<<(j-1)*i+i<<" ";
        }
        cout<<endl;
    }
}