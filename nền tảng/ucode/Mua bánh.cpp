#include<bits/stdc++.h>
#define int long long
using namespace std;
int n,m,k;
signed main(){
    cin>>n>>m>>k;
    
    // Trường hợp 1: Số bánh cần mua (n) đã đủ hoặc vượt mốc giảm giá (k)
    // Lúc này chắc chắn được giảm giá, và mua n cái là rẻ nhất (không cần so sánh với k cái vì k <= n)
    if (n >= k) {
        cout << (n * m) * 80 / 100;
    } 
    // Trường hợp 2: Số bánh cần mua (n) ít hơn mốc giảm giá (k)
    else {
        int s1 = n * m;                 // Mua đúng n cái (giá gốc)
        int s2 = (k * m) * 80 / 100;    // Mua cố lên k cái (để được giảm 20%)
        
        // So sánh xem cách nào rẻ hơn
        if (s1 < s2) cout << s1;
        else cout << s2;
    }
    
    return 0;
}