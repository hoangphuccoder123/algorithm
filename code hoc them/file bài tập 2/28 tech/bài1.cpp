//224A 
#include<iostream>
#include<cmath>
using namespace std; 
int main(){
    int a,b,c;
    cin>>a>>b>>c;
    // tính các cạnh xyz 
    double x= sqrt(1.0*a*c/b);
    double y= sqrt(1.0*a*b/c);
    double z= sqrt(1.0*b*c/a);
    int s=(4*(x+y+z)+0.5);
    cout<<s<<endl;
    return 0; 
}