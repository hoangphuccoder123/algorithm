#include<bits/stdc++.h>
#define int long long
using namespace std;
int n;
void stt(){
    vector<int>uoc;
    for(int i =1 ; i<=n/i;i++){
        if(n%i==0){
            uoc.push_back(i);
            if(i!=n/i) uoc.push_back(n/i);
        }
    }
    // sắp xếp tăng dần
    sort(uoc.begin(),uoc.end());
    for(int x:uoc) cout<<x<<" ";
    cout<<"\n";
}
int32_t main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin>>n;
    stt();
}
