#include<bits/stdc++.h>
#define int long long
using namespace std;
int n;
string s;
signed main(){
    cin>>n;
    cin>>s;
    
    string reversed = s;
    reverse(reversed.begin(), reversed.end());
    
    if (s==reversed){
        cout<<"YES";
    }
    else{
        cout << "NO";
    }
    
    return 0;
} 