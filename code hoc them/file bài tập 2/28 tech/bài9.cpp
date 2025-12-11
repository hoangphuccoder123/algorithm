#include<iostream>
using namespace std;
int main(){
    int d1, d2, d3; cin >> d1 >> d2 >> d3;
    int a=2*(d1+d2);
    int b=2*(d2+d3);
    int c=d1+d2+d3;
    int d=2*(d1+d3);
    int res =a;
    if(b<res)res=b;
    if(c<res)res=c;
    if(d<res)res=d;
    cout<<res<<endl;
    return 0;
} // 599A 