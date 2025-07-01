#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    
    while (t--) {
        long long a, b, c, d;
        cin >> a >> b >> c >> d;
        
        // Trường hợp 1: Hiệp sĩ của Flower đủ mạnh để giết Gellyfish
        if (d >= a) {
            cout << "Flower" << endl;
            continue;
        }
        
        // Trường hợp 2: Hiệp sĩ của Gellyfish đủ mạnh để giết Flower
        if (c >= b) {
            cout << "Gellyfish" << endl;
            continue;
        }
        
        // Trường hợp 3: Cả hai không đủ mạnh để giết đối thủ
        // Đây là phần quan trọng: Ai diệt được hiệp sĩ đối phương trước sẽ thắng
        
        // Tính toán số lượt cần thiết để giết hiệp sĩ đối phương
        long long turns_to_kill_flower_knight = (d + c - 1) / c; // Số lượt Gellyfish cần để giết hiệp sĩ Flower
        long long turns_to_kill_gelly_knight = (c + d - 1) / d; // Số lượt Flower cần để giết hiệp sĩ Gellyfish
        
        // Gellyfish đi trước nên có lợi thế
        if (turns_to_kill_flower_knight <= turns_to_kill_gelly_knight) {
            cout << "Gellyfish" << endl;
        } else {
            cout << "Flower" << endl;
        }
    }
    
    return 0;
}