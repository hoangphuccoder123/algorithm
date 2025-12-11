#include<iostream>//1061A 
using namespace std;
int main(){
    long long n, s;
    cin >> n >> s;
    long long so_xu = s / n + (s % n != 0);
    cout << so_xu;
    return 0;
} 