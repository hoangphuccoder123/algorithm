#include <bits/stdc++.h> 
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int a,b ; cin >> a >> b;
    char curr; 
    for (int i = 0 ; i<a ; i++){
        for (int j = 0 ; j<b ; j++){
            cin >> curr; 
            if (curr == 'C' || curr == 'M' || curr == 'Y' || curr == 'G') done=1;    
            }
        }
        cout <<"#"<<(done?"Color":"Black&White")<<"\n";
    }
}