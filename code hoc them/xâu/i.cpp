#include<iostream>
using namespace std;
string s;
int main(){
    getline(cin,s);
    int ans=1;
    for(char x : s){
        if (x==''){
            ans++;
        }
    }
    cout<<ans;
}