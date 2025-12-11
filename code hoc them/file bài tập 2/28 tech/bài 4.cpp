#include<iostream> // frog 
#include<cmath>
using namespace std;
int main(){
    long long a,b,k; 
    cin>>a>>b>>k;
    long long so_buoc=k/2;
    long long res1=1ll*so_buoc*(a-b);
    if(k%2==1){
        res1+=a;
    }
    cout<<res1<<endl; 
    return 0; 
}
