#include<bits/stdc++.h>
#define int long long 
using namespace std;
int n;
signed main(){
    cin>>n;
    double sum=0;
    for(int i=1;i<=n;i++){
        sum+=1.0/(i*i*i);
    }
    cout<<fixed<<setprecision(5)<<sum;
    return 0;
}