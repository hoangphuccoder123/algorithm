#include <iostream>
#include <string>
using namespace std;
string s;
int n;
char x;
int main(){
    cin >> n >> x; 
    cin >> s;       
    
    int count = 0;
    for(int i = 0; i < n; i++){  
        if(s[i] == x){
            count++;
        }
    }
    cout << count;
    return 0;
} 