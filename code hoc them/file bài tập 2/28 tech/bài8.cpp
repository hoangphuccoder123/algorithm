#include<iostream>//476A 
using namespace std;
int main(){
    int m;long long n;cin>>n>>m;
    long long min_moves=(n+1)/2;
    long long res=((min_moves+m-1)/m)*m;
    if(res>n) cout<<-1;
    else cout<<res;
    return 0;
}