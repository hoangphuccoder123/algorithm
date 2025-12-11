#include<iostream>
#include<vector>
using namespace std;
int main(){
    long long n; cin>>n;
    vector<long long> menh_gia={100,20,10,5,1};
    long long so_to=0;
    for(long long m:menh_gia){
        so_to+=n/m;
        n%=m;
        
    }
    cout<<so_to<<endl; 
    return 0;
}