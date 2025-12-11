#include<bits/stdc++.h>
#define int long long 
using namespace std;
const int N=1e6+5;
int n;
int a[N];
int32_t main(){
    cin>>n;
    for(int i=1; i<=n;i++){
        cin>>a[i];
    }
    int count=0;
    for(int i=2 ; i<=n-1;i++){ 
        if(a[i] >a[i-1] && a[i] > a[i+1] ){
            count++;
        }
    }
    cout<<count;
    return 0;
}
