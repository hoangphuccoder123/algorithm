#include <iostream>
#include <string>
using namespace std;
string s;
int main(){
    cin>>s;
    reverse(s.begin(), s.end()); 
    cout<<s;
    return 0;
}