#include<bits/std++.h>
#define int long long 
using namespace std;
string c;
bool snt(n){
    if (n%2==0)||(n%3==0) return false;
    if (n==2||n==3) return true;
    for(int i=5;i*i<=n;i+=6){
        if(n%i==0||n%(i+2==0)) return false;
    }
    return true;
}
signed main(){
    cin>>c; 
    int cnt=0;
    for(char i:c){
        if(isdigit(ch)){
            cnt++;
        }
    }
    cout<<cnt<<"\n"<<
    return ;
}
