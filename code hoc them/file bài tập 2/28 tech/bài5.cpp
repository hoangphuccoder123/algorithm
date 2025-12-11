//515A 
#include<iostream>
#include<vector>
using namespace std;
int main(){
    long long a,b,s;cin>>a>>b>>s;
    long long d=llabs(a)+llabs(b);// kcach để đi đúng đường 
    long long s_buoc=s-d; // số bước
    if(s_buoc%2==0 && d<=s){
        cout<<"Yes";
    }else{
        cout<<"No"; 
    }
    return 0;
}