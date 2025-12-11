#include<bits/stdc++.h>
#define int long long
using namespace std;
int n;
signed main(){
    cin>>n;
    for(int i=1 ; i<=n; i++){
        for(int j=1 ; j<=n;j++){
            if(i==1||i==n||j==1||j==n||i==j){
                cout<<"*";  // Bỏ khoảng trắng sau *
            }
            else{
                cout<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
} 