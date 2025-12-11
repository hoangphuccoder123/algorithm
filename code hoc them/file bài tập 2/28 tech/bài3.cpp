//1A
#include<iostream>
#include<cmath>
using namespace std;
int main(){
    long long n, m, a; 
    cin >> n >> m >> a;
    // Tính số viên theo từng chiều bằng chia làm tròn lên, rồi nhân lại
    long long b = (n + a - 1) / a; 
    long long c = (m + a - 1) / a;
    long long result = b * c;
    cout << result << endl;
    return 0;
}