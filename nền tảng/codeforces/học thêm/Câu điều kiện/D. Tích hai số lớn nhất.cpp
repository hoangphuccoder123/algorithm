#include<iostream>
#include<algorithm>
using namespace std; 
int main(){
    long long a,b,c;
    if(!(cin>>a>>b>>c)) return 0;
    int arr[3]={a,b,c};
    sort(arr,arr+3);
    cout<<arr[1] * arr[2] <<endl;
    return 0;
}