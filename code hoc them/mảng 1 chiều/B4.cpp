#include<bits/stdc++.h>
using namespace std;
const int N=1e6+5;
int n;
int a[N];
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin>>n;
    for (int i=1;i<=n;i++){
        cin>>a[i];
    }
    
    for(int i=1; i<n; i++){
        if((a[i]>0 && a[i+1]>0) || (a[i]<0 && a[i+1]<0)){
            cout<<a[i]<<" "<<a[i+1];
            return 0;
        }
    }
    return 0;
}